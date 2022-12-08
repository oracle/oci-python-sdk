# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OracleConnectionSummary(ConnectionSummary):
    """
    Summary of the Oracle Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OracleConnectionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.OracleConnectionSummary.connection_type` attribute
        of this class is ``ORACLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this OracleConnectionSummary.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS"
        :type connection_type: str

        :param id:
            The value to assign to the id property of this OracleConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OracleConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this OracleConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OracleConnectionSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OracleConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OracleConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OracleConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OracleConnectionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this OracleConnectionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this OracleConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OracleConnectionSummary.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this OracleConnectionSummary.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this OracleConnectionSummary.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this OracleConnectionSummary.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this OracleConnectionSummary.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this OracleConnectionSummary.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this OracleConnectionSummary.
        :type technology_type: str

        :param username:
            The value to assign to the username property of this OracleConnectionSummary.
        :type username: str

        :param connection_string:
            The value to assign to the connection_string property of this OracleConnectionSummary.
        :type connection_string: str

        :param session_mode:
            The value to assign to the session_mode property of this OracleConnectionSummary.
        :type session_mode: str

        :param private_ip:
            The value to assign to the private_ip property of this OracleConnectionSummary.
        :type private_ip: str

        :param database_id:
            The value to assign to the database_id property of this OracleConnectionSummary.
        :type database_id: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'username': 'str',
            'connection_string': 'str',
            'session_mode': 'str',
            'private_ip': 'str',
            'database_id': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'username': 'username',
            'connection_string': 'connectionString',
            'session_mode': 'sessionMode',
            'private_ip': 'privateIp',
            'database_id': 'databaseId'
        }

        self._connection_type = None
        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._ingress_ips = None
        self._nsg_ids = None
        self._technology_type = None
        self._username = None
        self._connection_string = None
        self._session_mode = None
        self._private_ip = None
        self._database_id = None
        self._connection_type = 'ORACLE'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this OracleConnectionSummary.
        The Oracle technology type.


        :return: The technology_type of this OracleConnectionSummary.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this OracleConnectionSummary.
        The Oracle technology type.


        :param technology_type: The technology_type of this OracleConnectionSummary.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def username(self):
        """
        **[Required]** Gets the username of this OracleConnectionSummary.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must
        already exist and be available for use by the database.  It must conform to the security
        requirements implemented by the database including length, case sensitivity, and so on.


        :return: The username of this OracleConnectionSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this OracleConnectionSummary.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must
        already exist and be available for use by the database.  It must conform to the security
        requirements implemented by the database including length, case sensitivity, and so on.


        :param username: The username of this OracleConnectionSummary.
        :type: str
        """
        self._username = username

    @property
    def connection_string(self):
        """
        Gets the connection_string of this OracleConnectionSummary.
        Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a
        database.


        :return: The connection_string of this OracleConnectionSummary.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this OracleConnectionSummary.
        Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a
        database.


        :param connection_string: The connection_string of this OracleConnectionSummary.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def session_mode(self):
        """
        Gets the session_mode of this OracleConnectionSummary.
        The mode of the database connection session to be established by the data client.
        'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
        Connection to a RAC database involves a redirection received from the SCAN listeners
        to the database node to connect to. By default the mode would be DIRECT.


        :return: The session_mode of this OracleConnectionSummary.
        :rtype: str
        """
        return self._session_mode

    @session_mode.setter
    def session_mode(self, session_mode):
        """
        Sets the session_mode of this OracleConnectionSummary.
        The mode of the database connection session to be established by the data client.
        'REDIRECT' - for a RAC database, 'DIRECT' - for a non-RAC database.
        Connection to a RAC database involves a redirection received from the SCAN listeners
        to the database node to connect to. By default the mode would be DIRECT.


        :param session_mode: The session_mode of this OracleConnectionSummary.
        :type: str
        """
        self._session_mode = session_mode

    @property
    def private_ip(self):
        """
        Gets the private_ip of this OracleConnectionSummary.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this OracleConnectionSummary.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this OracleConnectionSummary.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this OracleConnectionSummary.
        :type: str
        """
        self._private_ip = private_ip

    @property
    def database_id(self):
        """
        Gets the database_id of this OracleConnectionSummary.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this OracleConnectionSummary.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this OracleConnectionSummary.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this OracleConnectionSummary.
        :type: str
        """
        self._database_id = database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
