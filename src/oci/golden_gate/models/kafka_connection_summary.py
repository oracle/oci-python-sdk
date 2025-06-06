# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .connection_summary import ConnectionSummary
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KafkaConnectionSummary(ConnectionSummary):
    """
    Summary of the Kafka Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KafkaConnectionSummary object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.KafkaConnectionSummary.connection_type` attribute
        of this class is ``KAFKA`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this KafkaConnectionSummary.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG"
        :type connection_type: str

        :param id:
            The value to assign to the id property of this KafkaConnectionSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this KafkaConnectionSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this KafkaConnectionSummary.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this KafkaConnectionSummary.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this KafkaConnectionSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this KafkaConnectionSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this KafkaConnectionSummary.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this KafkaConnectionSummary.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this KafkaConnectionSummary.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this KafkaConnectionSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this KafkaConnectionSummary.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this KafkaConnectionSummary.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this KafkaConnectionSummary.
        :type key_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this KafkaConnectionSummary.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this KafkaConnectionSummary.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this KafkaConnectionSummary.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this KafkaConnectionSummary.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param locks:
            The value to assign to the locks property of this KafkaConnectionSummary.
        :type locks: list[oci.golden_gate.models.ResourceLock]

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this KafkaConnectionSummary.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this KafkaConnectionSummary.
        :type technology_type: str

        :param stream_pool_id:
            The value to assign to the stream_pool_id property of this KafkaConnectionSummary.
        :type stream_pool_id: str

        :param bootstrap_servers:
            The value to assign to the bootstrap_servers property of this KafkaConnectionSummary.
        :type bootstrap_servers: list[oci.golden_gate.models.KafkaBootstrapServer]

        :param security_protocol:
            The value to assign to the security_protocol property of this KafkaConnectionSummary.
        :type security_protocol: str

        :param username:
            The value to assign to the username property of this KafkaConnectionSummary.
        :type username: str

        :param password_secret_id:
            The value to assign to the password_secret_id property of this KafkaConnectionSummary.
        :type password_secret_id: str

        :param trust_store_secret_id:
            The value to assign to the trust_store_secret_id property of this KafkaConnectionSummary.
        :type trust_store_secret_id: str

        :param trust_store_password_secret_id:
            The value to assign to the trust_store_password_secret_id property of this KafkaConnectionSummary.
        :type trust_store_password_secret_id: str

        :param key_store_secret_id:
            The value to assign to the key_store_secret_id property of this KafkaConnectionSummary.
        :type key_store_secret_id: str

        :param key_store_password_secret_id:
            The value to assign to the key_store_password_secret_id property of this KafkaConnectionSummary.
        :type key_store_password_secret_id: str

        :param ssl_key_password_secret_id:
            The value to assign to the ssl_key_password_secret_id property of this KafkaConnectionSummary.
        :type ssl_key_password_secret_id: str

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
            'ingress_ips': 'list[IngressIpDetails]',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'locks': 'list[ResourceLock]',
            'does_use_secret_ids': 'bool',
            'technology_type': 'str',
            'stream_pool_id': 'str',
            'bootstrap_servers': 'list[KafkaBootstrapServer]',
            'security_protocol': 'str',
            'username': 'str',
            'password_secret_id': 'str',
            'trust_store_secret_id': 'str',
            'trust_store_password_secret_id': 'str',
            'key_store_secret_id': 'str',
            'key_store_password_secret_id': 'str',
            'ssl_key_password_secret_id': 'str'
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
            'ingress_ips': 'ingressIps',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'locks': 'locks',
            'does_use_secret_ids': 'doesUseSecretIds',
            'technology_type': 'technologyType',
            'stream_pool_id': 'streamPoolId',
            'bootstrap_servers': 'bootstrapServers',
            'security_protocol': 'securityProtocol',
            'username': 'username',
            'password_secret_id': 'passwordSecretId',
            'trust_store_secret_id': 'trustStoreSecretId',
            'trust_store_password_secret_id': 'trustStorePasswordSecretId',
            'key_store_secret_id': 'keyStoreSecretId',
            'key_store_password_secret_id': 'keyStorePasswordSecretId',
            'ssl_key_password_secret_id': 'sslKeyPasswordSecretId'
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
        self._ingress_ips = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._locks = None
        self._does_use_secret_ids = None
        self._technology_type = None
        self._stream_pool_id = None
        self._bootstrap_servers = None
        self._security_protocol = None
        self._username = None
        self._password_secret_id = None
        self._trust_store_secret_id = None
        self._trust_store_password_secret_id = None
        self._key_store_secret_id = None
        self._key_store_password_secret_id = None
        self._ssl_key_password_secret_id = None
        self._connection_type = 'KAFKA'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this KafkaConnectionSummary.
        The Kafka technology type.


        :return: The technology_type of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this KafkaConnectionSummary.
        The Kafka technology type.


        :param technology_type: The technology_type of this KafkaConnectionSummary.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def stream_pool_id(self):
        """
        Gets the stream_pool_id of this KafkaConnectionSummary.
        The `OCID`__ of the stream pool being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The stream_pool_id of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._stream_pool_id

    @stream_pool_id.setter
    def stream_pool_id(self, stream_pool_id):
        """
        Sets the stream_pool_id of this KafkaConnectionSummary.
        The `OCID`__ of the stream pool being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param stream_pool_id: The stream_pool_id of this KafkaConnectionSummary.
        :type: str
        """
        self._stream_pool_id = stream_pool_id

    @property
    def bootstrap_servers(self):
        """
        Gets the bootstrap_servers of this KafkaConnectionSummary.
        Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
        list of KafkaBootstrapServer objects specified by host/port.
        Used for establishing the initial connection to the Kafka cluster.
        Example: `\"server1.example.com:9092,server2.example.com:9092\"`


        :return: The bootstrap_servers of this KafkaConnectionSummary.
        :rtype: list[oci.golden_gate.models.KafkaBootstrapServer]
        """
        return self._bootstrap_servers

    @bootstrap_servers.setter
    def bootstrap_servers(self, bootstrap_servers):
        """
        Sets the bootstrap_servers of this KafkaConnectionSummary.
        Kafka bootstrap. Equivalent of bootstrap.servers configuration property in Kafka:
        list of KafkaBootstrapServer objects specified by host/port.
        Used for establishing the initial connection to the Kafka cluster.
        Example: `\"server1.example.com:9092,server2.example.com:9092\"`


        :param bootstrap_servers: The bootstrap_servers of this KafkaConnectionSummary.
        :type: list[oci.golden_gate.models.KafkaBootstrapServer]
        """
        self._bootstrap_servers = bootstrap_servers

    @property
    def security_protocol(self):
        """
        Gets the security_protocol of this KafkaConnectionSummary.
        Security Type for Kafka.


        :return: The security_protocol of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this KafkaConnectionSummary.
        Security Type for Kafka.


        :param security_protocol: The security_protocol of this KafkaConnectionSummary.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def username(self):
        """
        Gets the username of this KafkaConnectionSummary.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :return: The username of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this KafkaConnectionSummary.
        The username Oracle GoldenGate uses to connect the associated system of the given technology.
        This username must already exist and be available by the system/application to be connected to
        and must conform to the case sensitivty requirments defined in it.


        :param username: The username of this KafkaConnectionSummary.
        :type: str
        """
        self._username = username

    @property
    def password_secret_id(self):
        """
        Gets the password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The password_secret_id of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._password_secret_id

    @password_secret_id.setter
    def password_secret_id(self, password_secret_id):
        """
        Sets the password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the password is stored.
        The password Oracle GoldenGate uses to connect the associated system of the given technology.
        It must conform to the specific security requirements including length, case sensitivity, and so on.
        If secretId is used plaintext field must not be provided.
        Note: When provided, 'password' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param password_secret_id: The password_secret_id of this KafkaConnectionSummary.
        :type: str
        """
        self._password_secret_id = password_secret_id

    @property
    def trust_store_secret_id(self):
        """
        Gets the trust_store_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the content of the TrustStore file is stored.
        Note: When provided, 'trustStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The trust_store_secret_id of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._trust_store_secret_id

    @trust_store_secret_id.setter
    def trust_store_secret_id(self, trust_store_secret_id):
        """
        Sets the trust_store_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the content of the TrustStore file is stored.
        Note: When provided, 'trustStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param trust_store_secret_id: The trust_store_secret_id of this KafkaConnectionSummary.
        :type: str
        """
        self._trust_store_secret_id = trust_store_secret_id

    @property
    def trust_store_password_secret_id(self):
        """
        Gets the trust_store_password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the kafka TrustStore password is stored.
        Note: When provided, 'trustStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The trust_store_password_secret_id of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._trust_store_password_secret_id

    @trust_store_password_secret_id.setter
    def trust_store_password_secret_id(self, trust_store_password_secret_id):
        """
        Sets the trust_store_password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the kafka TrustStore password is stored.
        Note: When provided, 'trustStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param trust_store_password_secret_id: The trust_store_password_secret_id of this KafkaConnectionSummary.
        :type: str
        """
        self._trust_store_password_secret_id = trust_store_password_secret_id

    @property
    def key_store_secret_id(self):
        """
        Gets the key_store_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the content of the KeyStore file is stored.
        Note: When provided, 'keyStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_store_secret_id of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._key_store_secret_id

    @key_store_secret_id.setter
    def key_store_secret_id(self, key_store_secret_id):
        """
        Sets the key_store_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the content of the KeyStore file is stored.
        Note: When provided, 'keyStore' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_store_secret_id: The key_store_secret_id of this KafkaConnectionSummary.
        :type: str
        """
        self._key_store_secret_id = key_store_secret_id

    @property
    def key_store_password_secret_id(self):
        """
        Gets the key_store_password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the kafka KeyStore password is stored.
        Note: When provided, 'keyStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_store_password_secret_id of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._key_store_password_secret_id

    @key_store_password_secret_id.setter
    def key_store_password_secret_id(self, key_store_password_secret_id):
        """
        Sets the key_store_password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the kafka KeyStore password is stored.
        Note: When provided, 'keyStorePassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_store_password_secret_id: The key_store_password_secret_id of this KafkaConnectionSummary.
        :type: str
        """
        self._key_store_password_secret_id = key_store_password_secret_id

    @property
    def ssl_key_password_secret_id(self):
        """
        Gets the ssl_key_password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the kafka Ssl Key password is stored.
        Note: When provided, 'sslKeyPassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The ssl_key_password_secret_id of this KafkaConnectionSummary.
        :rtype: str
        """
        return self._ssl_key_password_secret_id

    @ssl_key_password_secret_id.setter
    def ssl_key_password_secret_id(self, ssl_key_password_secret_id):
        """
        Sets the ssl_key_password_secret_id of this KafkaConnectionSummary.
        The `OCID`__ of the Secret where the kafka Ssl Key password is stored.
        Note: When provided, 'sslKeyPassword' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param ssl_key_password_secret_id: The ssl_key_password_secret_id of this KafkaConnectionSummary.
        :type: str
        """
        self._ssl_key_password_secret_id = ssl_key_password_secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
