# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataGuardAssociationSummary(object):
    """
    The properties that define a Data Guard association.

    To use any of the API operations, you must be authorized in an IAM policy. If you're not authorized, talk to an
    administrator. If you're an administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    For information about endpoints and signing API requests, see
    `About the API`__. For information about available SDKs and tools, see
    `SDKS and Other Tools`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    __ https://docs.cloud.oracle.com/Content/API/Concepts/usingapi.htm
    __ https://docs.cloud.oracle.com/Content/API/Concepts/sdks.htm
    """

    #: A constant which can be used with the role property of a DataGuardAssociationSummary.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a DataGuardAssociationSummary.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a DataGuardAssociationSummary.
    #: This constant has a value of "DISABLED_STANDBY"
    ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    #: A constant which can be used with the lifecycle_state property of a DataGuardAssociationSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a DataGuardAssociationSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a DataGuardAssociationSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DataGuardAssociationSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a DataGuardAssociationSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a DataGuardAssociationSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the peer_role property of a DataGuardAssociationSummary.
    #: This constant has a value of "PRIMARY"
    PEER_ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the peer_role property of a DataGuardAssociationSummary.
    #: This constant has a value of "STANDBY"
    PEER_ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the peer_role property of a DataGuardAssociationSummary.
    #: This constant has a value of "DISABLED_STANDBY"
    PEER_ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    #: A constant which can be used with the protection_mode property of a DataGuardAssociationSummary.
    #: This constant has a value of "MAXIMUM_AVAILABILITY"
    PROTECTION_MODE_MAXIMUM_AVAILABILITY = "MAXIMUM_AVAILABILITY"

    #: A constant which can be used with the protection_mode property of a DataGuardAssociationSummary.
    #: This constant has a value of "MAXIMUM_PERFORMANCE"
    PROTECTION_MODE_MAXIMUM_PERFORMANCE = "MAXIMUM_PERFORMANCE"

    #: A constant which can be used with the protection_mode property of a DataGuardAssociationSummary.
    #: This constant has a value of "MAXIMUM_PROTECTION"
    PROTECTION_MODE_MAXIMUM_PROTECTION = "MAXIMUM_PROTECTION"

    #: A constant which can be used with the transport_type property of a DataGuardAssociationSummary.
    #: This constant has a value of "SYNC"
    TRANSPORT_TYPE_SYNC = "SYNC"

    #: A constant which can be used with the transport_type property of a DataGuardAssociationSummary.
    #: This constant has a value of "ASYNC"
    TRANSPORT_TYPE_ASYNC = "ASYNC"

    #: A constant which can be used with the transport_type property of a DataGuardAssociationSummary.
    #: This constant has a value of "FASTSYNC"
    TRANSPORT_TYPE_FASTSYNC = "FASTSYNC"

    def __init__(self, **kwargs):
        """
        Initializes a new DataGuardAssociationSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DataGuardAssociationSummary.
        :type id: str

        :param database_id:
            The value to assign to the database_id property of this DataGuardAssociationSummary.
        :type database_id: str

        :param role:
            The value to assign to the role property of this DataGuardAssociationSummary.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DataGuardAssociationSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DataGuardAssociationSummary.
        :type lifecycle_details: str

        :param peer_db_system_id:
            The value to assign to the peer_db_system_id property of this DataGuardAssociationSummary.
        :type peer_db_system_id: str

        :param peer_db_home_id:
            The value to assign to the peer_db_home_id property of this DataGuardAssociationSummary.
        :type peer_db_home_id: str

        :param peer_database_id:
            The value to assign to the peer_database_id property of this DataGuardAssociationSummary.
        :type peer_database_id: str

        :param peer_data_guard_association_id:
            The value to assign to the peer_data_guard_association_id property of this DataGuardAssociationSummary.
        :type peer_data_guard_association_id: str

        :param peer_role:
            The value to assign to the peer_role property of this DataGuardAssociationSummary.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type peer_role: str

        :param apply_lag:
            The value to assign to the apply_lag property of this DataGuardAssociationSummary.
        :type apply_lag: str

        :param apply_rate:
            The value to assign to the apply_rate property of this DataGuardAssociationSummary.
        :type apply_rate: str

        :param protection_mode:
            The value to assign to the protection_mode property of this DataGuardAssociationSummary.
            Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protection_mode: str

        :param transport_type:
            The value to assign to the transport_type property of this DataGuardAssociationSummary.
            Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type transport_type: str

        :param time_created:
            The value to assign to the time_created property of this DataGuardAssociationSummary.
        :type time_created: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'database_id': 'str',
            'role': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'peer_db_system_id': 'str',
            'peer_db_home_id': 'str',
            'peer_database_id': 'str',
            'peer_data_guard_association_id': 'str',
            'peer_role': 'str',
            'apply_lag': 'str',
            'apply_rate': 'str',
            'protection_mode': 'str',
            'transport_type': 'str',
            'time_created': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'database_id': 'databaseId',
            'role': 'role',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'peer_db_system_id': 'peerDbSystemId',
            'peer_db_home_id': 'peerDbHomeId',
            'peer_database_id': 'peerDatabaseId',
            'peer_data_guard_association_id': 'peerDataGuardAssociationId',
            'peer_role': 'peerRole',
            'apply_lag': 'applyLag',
            'apply_rate': 'applyRate',
            'protection_mode': 'protectionMode',
            'transport_type': 'transportType',
            'time_created': 'timeCreated'
        }

        self._id = None
        self._database_id = None
        self._role = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._peer_db_system_id = None
        self._peer_db_home_id = None
        self._peer_database_id = None
        self._peer_data_guard_association_id = None
        self._peer_role = None
        self._apply_lag = None
        self._apply_rate = None
        self._protection_mode = None
        self._transport_type = None
        self._time_created = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DataGuardAssociationSummary.
        The `OCID`__ of the Data Guard association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataGuardAssociationSummary.
        The `OCID`__ of the Data Guard association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DataGuardAssociationSummary.
        :type: str
        """
        self._id = id

    @property
    def database_id(self):
        """
        **[Required]** Gets the database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the reporting database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the reporting database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def role(self):
        """
        **[Required]** Gets the role of this DataGuardAssociationSummary.
        The role of the reporting database in this Data Guard association.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this DataGuardAssociationSummary.
        The role of the reporting database in this Data Guard association.


        :param role: The role of this DataGuardAssociationSummary.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DataGuardAssociationSummary.
        The current state of the Data Guard association.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DataGuardAssociationSummary.
        The current state of the Data Guard association.


        :param lifecycle_state: The lifecycle_state of this DataGuardAssociationSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "TERMINATING", "TERMINATED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DataGuardAssociationSummary.
        Additional information about the current lifecycleState, if available.


        :return: The lifecycle_details of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DataGuardAssociationSummary.
        Additional information about the current lifecycleState, if available.


        :param lifecycle_details: The lifecycle_details of this DataGuardAssociationSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def peer_db_system_id(self):
        """
        **[Required]** Gets the peer_db_system_id of this DataGuardAssociationSummary.
        The `OCID`__ of the DB system containing the associated
        peer database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_system_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_db_system_id

    @peer_db_system_id.setter
    def peer_db_system_id(self, peer_db_system_id):
        """
        Sets the peer_db_system_id of this DataGuardAssociationSummary.
        The `OCID`__ of the DB system containing the associated
        peer database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_db_system_id: The peer_db_system_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_db_system_id = peer_db_system_id

    @property
    def peer_db_home_id(self):
        """
        Gets the peer_db_home_id of this DataGuardAssociationSummary.
        The `OCID`__ of the Database Home containing the associated peer database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_home_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_db_home_id

    @peer_db_home_id.setter
    def peer_db_home_id(self, peer_db_home_id):
        """
        Sets the peer_db_home_id of this DataGuardAssociationSummary.
        The `OCID`__ of the Database Home containing the associated peer database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_db_home_id: The peer_db_home_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_db_home_id = peer_db_home_id

    @property
    def peer_database_id(self):
        """
        Gets the peer_database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the associated peer database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_database_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_database_id

    @peer_database_id.setter
    def peer_database_id(self, peer_database_id):
        """
        Sets the peer_database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the associated peer database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_database_id: The peer_database_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_database_id = peer_database_id

    @property
    def peer_data_guard_association_id(self):
        """
        Gets the peer_data_guard_association_id of this DataGuardAssociationSummary.
        The `OCID`__ of the peer database's Data Guard association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_data_guard_association_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_data_guard_association_id

    @peer_data_guard_association_id.setter
    def peer_data_guard_association_id(self, peer_data_guard_association_id):
        """
        Sets the peer_data_guard_association_id of this DataGuardAssociationSummary.
        The `OCID`__ of the peer database's Data Guard association.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_data_guard_association_id: The peer_data_guard_association_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_data_guard_association_id = peer_data_guard_association_id

    @property
    def peer_role(self):
        """
        **[Required]** Gets the peer_role of this DataGuardAssociationSummary.
        The role of the peer database in this Data Guard association.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The peer_role of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_role

    @peer_role.setter
    def peer_role(self, peer_role):
        """
        Sets the peer_role of this DataGuardAssociationSummary.
        The role of the peer database in this Data Guard association.


        :param peer_role: The peer_role of this DataGuardAssociationSummary.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY"]
        if not value_allowed_none_or_none_sentinel(peer_role, allowed_values):
            peer_role = 'UNKNOWN_ENUM_VALUE'
        self._peer_role = peer_role

    @property
    def apply_lag(self):
        """
        Gets the apply_lag of this DataGuardAssociationSummary.
        The lag time between updates to the primary database and application of the redo data on the standby database,
        as computed by the reporting database.

        Example: `9 seconds`


        :return: The apply_lag of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._apply_lag

    @apply_lag.setter
    def apply_lag(self, apply_lag):
        """
        Sets the apply_lag of this DataGuardAssociationSummary.
        The lag time between updates to the primary database and application of the redo data on the standby database,
        as computed by the reporting database.

        Example: `9 seconds`


        :param apply_lag: The apply_lag of this DataGuardAssociationSummary.
        :type: str
        """
        self._apply_lag = apply_lag

    @property
    def apply_rate(self):
        """
        Gets the apply_rate of this DataGuardAssociationSummary.
        The rate at which redo logs are synced between the associated databases.

        Example: `180 Mb per second`


        :return: The apply_rate of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._apply_rate

    @apply_rate.setter
    def apply_rate(self, apply_rate):
        """
        Sets the apply_rate of this DataGuardAssociationSummary.
        The rate at which redo logs are synced between the associated databases.

        Example: `180 Mb per second`


        :param apply_rate: The apply_rate of this DataGuardAssociationSummary.
        :type: str
        """
        self._apply_rate = apply_rate

    @property
    def protection_mode(self):
        """
        **[Required]** Gets the protection_mode of this DataGuardAssociationSummary.
        The protection mode of this Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000

        Allowed values for this property are: "MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protection_mode of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """
        Sets the protection_mode of this DataGuardAssociationSummary.
        The protection mode of this Data Guard association. For more information, see
        `Oracle Data Guard Protection Modes`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-protection-modes.htm#SBYDB02000


        :param protection_mode: The protection_mode of this DataGuardAssociationSummary.
        :type: str
        """
        allowed_values = ["MAXIMUM_AVAILABILITY", "MAXIMUM_PERFORMANCE", "MAXIMUM_PROTECTION"]
        if not value_allowed_none_or_none_sentinel(protection_mode, allowed_values):
            protection_mode = 'UNKNOWN_ENUM_VALUE'
        self._protection_mode = protection_mode

    @property
    def transport_type(self):
        """
        Gets the transport_type of this DataGuardAssociationSummary.
        The redo transport type used by this Data Guard association.  For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400

        Allowed values for this property are: "SYNC", "ASYNC", "FASTSYNC", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The transport_type of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._transport_type

    @transport_type.setter
    def transport_type(self, transport_type):
        """
        Sets the transport_type of this DataGuardAssociationSummary.
        The redo transport type used by this Data Guard association.  For more information, see
        `Redo Transport Services`__
        in the Oracle Data Guard documentation.

        __ http://docs.oracle.com/database/122/SBYDB/oracle-data-guard-redo-transport-services.htm#SBYDB00400


        :param transport_type: The transport_type of this DataGuardAssociationSummary.
        :type: str
        """
        allowed_values = ["SYNC", "ASYNC", "FASTSYNC"]
        if not value_allowed_none_or_none_sentinel(transport_type, allowed_values):
            transport_type = 'UNKNOWN_ENUM_VALUE'
        self._transport_type = transport_type

    @property
    def time_created(self):
        """
        Gets the time_created of this DataGuardAssociationSummary.
        The date and time the Data Guard association was created.


        :return: The time_created of this DataGuardAssociationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataGuardAssociationSummary.
        The date and time the Data Guard association was created.


        :param time_created: The time_created of this DataGuardAssociationSummary.
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
