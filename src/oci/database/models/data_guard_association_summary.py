# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class DataGuardAssociationSummary(object):

    def __init__(self):

        self.swagger_types = {
            'apply_lag': 'str',
            'apply_rate': 'str',
            'database_id': 'str',
            'id': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'peer_data_guard_association_id': 'str',
            'peer_database_id': 'str',
            'peer_db_home_id': 'str',
            'peer_db_system_id': 'str',
            'peer_role': 'str',
            'protection_mode': 'str',
            'role': 'str',
            'time_created': 'datetime',
            'transport_type': 'str'
        }

        self.attribute_map = {
            'apply_lag': 'applyLag',
            'apply_rate': 'applyRate',
            'database_id': 'databaseId',
            'id': 'id',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'peer_data_guard_association_id': 'peerDataGuardAssociationId',
            'peer_database_id': 'peerDatabaseId',
            'peer_db_home_id': 'peerDbHomeId',
            'peer_db_system_id': 'peerDbSystemId',
            'peer_role': 'peerRole',
            'protection_mode': 'protectionMode',
            'role': 'role',
            'time_created': 'timeCreated',
            'transport_type': 'transportType'
        }

        self._apply_lag = None
        self._apply_rate = None
        self._database_id = None
        self._id = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._peer_data_guard_association_id = None
        self._peer_database_id = None
        self._peer_db_home_id = None
        self._peer_db_system_id = None
        self._peer_role = None
        self._protection_mode = None
        self._role = None
        self._time_created = None
        self._transport_type = None

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
    def database_id(self):
        """
        Gets the database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the reporting database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the reporting database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._database_id = database_id

    @property
    def id(self):
        """
        Gets the id of this DataGuardAssociationSummary.
        The `OCID`__ of the Data Guard association.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DataGuardAssociationSummary.
        The `OCID`__ of the Data Guard association.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DataGuardAssociationSummary.
        :type: str
        """
        self._id = id

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
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DataGuardAssociationSummary.
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
        if lifecycle_state not in allowed_values:
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def peer_data_guard_association_id(self):
        """
        Gets the peer_data_guard_association_id of this DataGuardAssociationSummary.
        The `OCID`__ of the peer database's Data Guard association.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The peer_data_guard_association_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_data_guard_association_id

    @peer_data_guard_association_id.setter
    def peer_data_guard_association_id(self, peer_data_guard_association_id):
        """
        Sets the peer_data_guard_association_id of this DataGuardAssociationSummary.
        The `OCID`__ of the peer database's Data Guard association.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param peer_data_guard_association_id: The peer_data_guard_association_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_data_guard_association_id = peer_data_guard_association_id

    @property
    def peer_database_id(self):
        """
        Gets the peer_database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the associated peer database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The peer_database_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_database_id

    @peer_database_id.setter
    def peer_database_id(self, peer_database_id):
        """
        Sets the peer_database_id of this DataGuardAssociationSummary.
        The `OCID`__ of the associated peer database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param peer_database_id: The peer_database_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_database_id = peer_database_id

    @property
    def peer_db_home_id(self):
        """
        Gets the peer_db_home_id of this DataGuardAssociationSummary.
        The `OCID`__ of the database home containing the associated peer database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_home_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_db_home_id

    @peer_db_home_id.setter
    def peer_db_home_id(self, peer_db_home_id):
        """
        Sets the peer_db_home_id of this DataGuardAssociationSummary.
        The `OCID`__ of the database home containing the associated peer database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param peer_db_home_id: The peer_db_home_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_db_home_id = peer_db_home_id

    @property
    def peer_db_system_id(self):
        """
        Gets the peer_db_system_id of this DataGuardAssociationSummary.
        The `OCID`__ of the DB System containing the associated
        peer database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_system_id of this DataGuardAssociationSummary.
        :rtype: str
        """
        return self._peer_db_system_id

    @peer_db_system_id.setter
    def peer_db_system_id(self, peer_db_system_id):
        """
        Sets the peer_db_system_id of this DataGuardAssociationSummary.
        The `OCID`__ of the DB System containing the associated
        peer database.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param peer_db_system_id: The peer_db_system_id of this DataGuardAssociationSummary.
        :type: str
        """
        self._peer_db_system_id = peer_db_system_id

    @property
    def peer_role(self):
        """
        Gets the peer_role of this DataGuardAssociationSummary.
        The role of the peer database in this Data Guard association.

        Allowed values for this property are: "PRIMARY", "STANDBY", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["PRIMARY", "STANDBY"]
        if peer_role not in allowed_values:
            peer_role = 'UNKNOWN_ENUM_VALUE'
        self._peer_role = peer_role

    @property
    def protection_mode(self):
        """
        Gets the protection_mode of this DataGuardAssociationSummary.
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
        if protection_mode not in allowed_values:
            protection_mode = 'UNKNOWN_ENUM_VALUE'
        self._protection_mode = protection_mode

    @property
    def role(self):
        """
        Gets the role of this DataGuardAssociationSummary.
        The role of the reporting database in this Data Guard association.

        Allowed values for this property are: "PRIMARY", "STANDBY", 'UNKNOWN_ENUM_VALUE'.
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
        allowed_values = ["PRIMARY", "STANDBY"]
        if role not in allowed_values:
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def time_created(self):
        """
        Gets the time_created of this DataGuardAssociationSummary.
        The date and time the Data Guard Association was created.


        :return: The time_created of this DataGuardAssociationSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DataGuardAssociationSummary.
        The date and time the Data Guard Association was created.


        :param time_created: The time_created of this DataGuardAssociationSummary.
        :type: datetime
        """
        self._time_created = time_created

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
        if transport_type not in allowed_values:
            transport_type = 'UNKNOWN_ENUM_VALUE'
        self._transport_type = transport_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
