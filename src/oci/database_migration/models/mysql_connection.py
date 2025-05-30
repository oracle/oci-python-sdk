# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20230518

from .connection import Connection
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MysqlConnection(Connection):
    """
    Represents the metadata of a MySQL Connection.
    """

    #: A constant which can be used with the technology_type property of a MysqlConnection.
    #: This constant has a value of "AMAZON_AURORA_MYSQL"
    TECHNOLOGY_TYPE_AMAZON_AURORA_MYSQL = "AMAZON_AURORA_MYSQL"

    #: A constant which can be used with the technology_type property of a MysqlConnection.
    #: This constant has a value of "AMAZON_RDS_MYSQL"
    TECHNOLOGY_TYPE_AMAZON_RDS_MYSQL = "AMAZON_RDS_MYSQL"

    #: A constant which can be used with the technology_type property of a MysqlConnection.
    #: This constant has a value of "AZURE_MYSQL"
    TECHNOLOGY_TYPE_AZURE_MYSQL = "AZURE_MYSQL"

    #: A constant which can be used with the technology_type property of a MysqlConnection.
    #: This constant has a value of "GOOGLE_CLOUD_SQL_MYSQL"
    TECHNOLOGY_TYPE_GOOGLE_CLOUD_SQL_MYSQL = "GOOGLE_CLOUD_SQL_MYSQL"

    #: A constant which can be used with the technology_type property of a MysqlConnection.
    #: This constant has a value of "MYSQL_SERVER"
    TECHNOLOGY_TYPE_MYSQL_SERVER = "MYSQL_SERVER"

    #: A constant which can be used with the technology_type property of a MysqlConnection.
    #: This constant has a value of "OCI_MYSQL"
    TECHNOLOGY_TYPE_OCI_MYSQL = "OCI_MYSQL"

    #: A constant which can be used with the security_protocol property of a MysqlConnection.
    #: This constant has a value of "PLAIN"
    SECURITY_PROTOCOL_PLAIN = "PLAIN"

    #: A constant which can be used with the security_protocol property of a MysqlConnection.
    #: This constant has a value of "TLS"
    SECURITY_PROTOCOL_TLS = "TLS"

    #: A constant which can be used with the security_protocol property of a MysqlConnection.
    #: This constant has a value of "MTLS"
    SECURITY_PROTOCOL_MTLS = "MTLS"

    #: A constant which can be used with the ssl_mode property of a MysqlConnection.
    #: This constant has a value of "DISABLED"
    SSL_MODE_DISABLED = "DISABLED"

    #: A constant which can be used with the ssl_mode property of a MysqlConnection.
    #: This constant has a value of "PREFERRED"
    SSL_MODE_PREFERRED = "PREFERRED"

    #: A constant which can be used with the ssl_mode property of a MysqlConnection.
    #: This constant has a value of "REQUIRED"
    SSL_MODE_REQUIRED = "REQUIRED"

    #: A constant which can be used with the ssl_mode property of a MysqlConnection.
    #: This constant has a value of "VERIFY_CA"
    SSL_MODE_VERIFY_CA = "VERIFY_CA"

    #: A constant which can be used with the ssl_mode property of a MysqlConnection.
    #: This constant has a value of "VERIFY_IDENTITY"
    SSL_MODE_VERIFY_IDENTITY = "VERIFY_IDENTITY"

    def __init__(self, **kwargs):
        """
        Initializes a new MysqlConnection object with values from keyword arguments. The default value of the :py:attr:`~oci.database_migration.models.MysqlConnection.connection_type` attribute
        of this class is ``MYSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this MysqlConnection.
            Allowed values for this property are: "MYSQL", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this MysqlConnection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this MysqlConnection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this MysqlConnection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MysqlConnection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MysqlConnection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MysqlConnection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MysqlConnection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MysqlConnection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this MysqlConnection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this MysqlConnection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this MysqlConnection.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this MysqlConnection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this MysqlConnection.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this MysqlConnection.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this MysqlConnection.
        :type ingress_ips: list[oci.database_migration.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this MysqlConnection.
        :type nsg_ids: list[str]

        :param username:
            The value to assign to the username property of this MysqlConnection.
        :type username: str

        :param password:
            The value to assign to the password property of this MysqlConnection.
        :type password: str

        :param replication_username:
            The value to assign to the replication_username property of this MysqlConnection.
        :type replication_username: str

        :param replication_password:
            The value to assign to the replication_password property of this MysqlConnection.
        :type replication_password: str

        :param secret_id:
            The value to assign to the secret_id property of this MysqlConnection.
        :type secret_id: str

        :param private_endpoint_id:
            The value to assign to the private_endpoint_id property of this MysqlConnection.
        :type private_endpoint_id: str

        :param technology_type:
            The value to assign to the technology_type property of this MysqlConnection.
            Allowed values for this property are: "AMAZON_AURORA_MYSQL", "AMAZON_RDS_MYSQL", "AZURE_MYSQL", "GOOGLE_CLOUD_SQL_MYSQL", "MYSQL_SERVER", "OCI_MYSQL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type technology_type: str

        :param host:
            The value to assign to the host property of this MysqlConnection.
        :type host: str

        :param port:
            The value to assign to the port property of this MysqlConnection.
        :type port: int

        :param database_name:
            The value to assign to the database_name property of this MysqlConnection.
        :type database_name: str

        :param security_protocol:
            The value to assign to the security_protocol property of this MysqlConnection.
            Allowed values for this property are: "PLAIN", "TLS", "MTLS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type security_protocol: str

        :param ssl_mode:
            The value to assign to the ssl_mode property of this MysqlConnection.
            Allowed values for this property are: "DISABLED", "PREFERRED", "REQUIRED", "VERIFY_CA", "VERIFY_IDENTITY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type ssl_mode: str

        :param additional_attributes:
            The value to assign to the additional_attributes property of this MysqlConnection.
        :type additional_attributes: list[oci.database_migration.models.NameValuePair]

        :param db_system_id:
            The value to assign to the db_system_id property of this MysqlConnection.
        :type db_system_id: str

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
            'username': 'str',
            'password': 'str',
            'replication_username': 'str',
            'replication_password': 'str',
            'secret_id': 'str',
            'private_endpoint_id': 'str',
            'technology_type': 'str',
            'host': 'str',
            'port': 'int',
            'database_name': 'str',
            'security_protocol': 'str',
            'ssl_mode': 'str',
            'additional_attributes': 'list[NameValuePair]',
            'db_system_id': 'str'
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
            'username': 'username',
            'password': 'password',
            'replication_username': 'replicationUsername',
            'replication_password': 'replicationPassword',
            'secret_id': 'secretId',
            'private_endpoint_id': 'privateEndpointId',
            'technology_type': 'technologyType',
            'host': 'host',
            'port': 'port',
            'database_name': 'databaseName',
            'security_protocol': 'securityProtocol',
            'ssl_mode': 'sslMode',
            'additional_attributes': 'additionalAttributes',
            'db_system_id': 'dbSystemId'
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
        self._username = None
        self._password = None
        self._replication_username = None
        self._replication_password = None
        self._secret_id = None
        self._private_endpoint_id = None
        self._technology_type = None
        self._host = None
        self._port = None
        self._database_name = None
        self._security_protocol = None
        self._ssl_mode = None
        self._additional_attributes = None
        self._db_system_id = None
        self._connection_type = 'MYSQL'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this MysqlConnection.
        The type of MySQL source or target connection.
        Example: OCI_MYSQL represents OCI MySQL HeatWave Database Service

        Allowed values for this property are: "AMAZON_AURORA_MYSQL", "AMAZON_RDS_MYSQL", "AZURE_MYSQL", "GOOGLE_CLOUD_SQL_MYSQL", "MYSQL_SERVER", "OCI_MYSQL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The technology_type of this MysqlConnection.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this MysqlConnection.
        The type of MySQL source or target connection.
        Example: OCI_MYSQL represents OCI MySQL HeatWave Database Service


        :param technology_type: The technology_type of this MysqlConnection.
        :type: str
        """
        allowed_values = ["AMAZON_AURORA_MYSQL", "AMAZON_RDS_MYSQL", "AZURE_MYSQL", "GOOGLE_CLOUD_SQL_MYSQL", "MYSQL_SERVER", "OCI_MYSQL"]
        if not value_allowed_none_or_none_sentinel(technology_type, allowed_values):
            technology_type = 'UNKNOWN_ENUM_VALUE'
        self._technology_type = technology_type

    @property
    def host(self):
        """
        Gets the host of this MysqlConnection.
        The IP Address of the host.


        :return: The host of this MysqlConnection.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this MysqlConnection.
        The IP Address of the host.


        :param host: The host of this MysqlConnection.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        Gets the port of this MysqlConnection.
        The port to be used for the connection.


        :return: The port of this MysqlConnection.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this MysqlConnection.
        The port to be used for the connection.


        :param port: The port of this MysqlConnection.
        :type: int
        """
        self._port = port

    @property
    def database_name(self):
        """
        Gets the database_name of this MysqlConnection.
        The name of the database being referenced.


        :return: The database_name of this MysqlConnection.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this MysqlConnection.
        The name of the database being referenced.


        :param database_name: The database_name of this MysqlConnection.
        :type: str
        """
        self._database_name = database_name

    @property
    def security_protocol(self):
        """
        **[Required]** Gets the security_protocol of this MysqlConnection.
        Security Protocol to be used for the connection.

        Allowed values for this property are: "PLAIN", "TLS", "MTLS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The security_protocol of this MysqlConnection.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this MysqlConnection.
        Security Protocol to be used for the connection.


        :param security_protocol: The security_protocol of this MysqlConnection.
        :type: str
        """
        allowed_values = ["PLAIN", "TLS", "MTLS"]
        if not value_allowed_none_or_none_sentinel(security_protocol, allowed_values):
            security_protocol = 'UNKNOWN_ENUM_VALUE'
        self._security_protocol = security_protocol

    @property
    def ssl_mode(self):
        """
        Gets the ssl_mode of this MysqlConnection.
        SSL mode to be used for the connection.

        Allowed values for this property are: "DISABLED", "PREFERRED", "REQUIRED", "VERIFY_CA", "VERIFY_IDENTITY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The ssl_mode of this MysqlConnection.
        :rtype: str
        """
        return self._ssl_mode

    @ssl_mode.setter
    def ssl_mode(self, ssl_mode):
        """
        Sets the ssl_mode of this MysqlConnection.
        SSL mode to be used for the connection.


        :param ssl_mode: The ssl_mode of this MysqlConnection.
        :type: str
        """
        allowed_values = ["DISABLED", "PREFERRED", "REQUIRED", "VERIFY_CA", "VERIFY_IDENTITY"]
        if not value_allowed_none_or_none_sentinel(ssl_mode, allowed_values):
            ssl_mode = 'UNKNOWN_ENUM_VALUE'
        self._ssl_mode = ssl_mode

    @property
    def additional_attributes(self):
        """
        Gets the additional_attributes of this MysqlConnection.
        An array of name-value pair attribute entries.


        :return: The additional_attributes of this MysqlConnection.
        :rtype: list[oci.database_migration.models.NameValuePair]
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """
        Sets the additional_attributes of this MysqlConnection.
        An array of name-value pair attribute entries.


        :param additional_attributes: The additional_attributes of this MysqlConnection.
        :type: list[oci.database_migration.models.NameValuePair]
        """
        self._additional_attributes = additional_attributes

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this MysqlConnection.
        The OCID of the database system being referenced.


        :return: The db_system_id of this MysqlConnection.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this MysqlConnection.
        The OCID of the database system being referenced.


        :param db_system_id: The db_system_id of this MysqlConnection.
        :type: str
        """
        self._db_system_id = db_system_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
