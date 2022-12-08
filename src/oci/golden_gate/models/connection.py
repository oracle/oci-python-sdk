# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Connection(object):
    """
    Represents the metadata description of a connection used by deployments in the same compartment.
    """

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "GOLDENGATE"
    CONNECTION_TYPE_GOLDENGATE = "GOLDENGATE"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "KAFKA"
    CONNECTION_TYPE_KAFKA = "KAFKA"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "KAFKA_SCHEMA_REGISTRY"
    CONNECTION_TYPE_KAFKA_SCHEMA_REGISTRY = "KAFKA_SCHEMA_REGISTRY"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "MYSQL"
    CONNECTION_TYPE_MYSQL = "MYSQL"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "OCI_OBJECT_STORAGE"
    CONNECTION_TYPE_OCI_OBJECT_STORAGE = "OCI_OBJECT_STORAGE"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "ORACLE"
    CONNECTION_TYPE_ORACLE = "ORACLE"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "AZURE_DATA_LAKE_STORAGE"
    CONNECTION_TYPE_AZURE_DATA_LAKE_STORAGE = "AZURE_DATA_LAKE_STORAGE"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "POSTGRESQL"
    CONNECTION_TYPE_POSTGRESQL = "POSTGRESQL"

    #: A constant which can be used with the connection_type property of a Connection.
    #: This constant has a value of "AZURE_SYNAPSE_ANALYTICS"
    CONNECTION_TYPE_AZURE_SYNAPSE_ANALYTICS = "AZURE_SYNAPSE_ANALYTICS"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Connection.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Connection object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.golden_gate.models.KafkaConnection`
        * :class:`~oci.golden_gate.models.PostgresqlConnection`
        * :class:`~oci.golden_gate.models.OciObjectStorageConnection`
        * :class:`~oci.golden_gate.models.KafkaSchemaRegistryConnection`
        * :class:`~oci.golden_gate.models.GoldenGateConnection`
        * :class:`~oci.golden_gate.models.MysqlConnection`
        * :class:`~oci.golden_gate.models.OracleConnection`
        * :class:`~oci.golden_gate.models.AzureDataLakeStorageConnection`
        * :class:`~oci.golden_gate.models.AzureSynapseConnection`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this Connection.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type connection_type: str

        :param id:
            The value to assign to the id property of this Connection.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Connection.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Connection.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Connection.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Connection.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Connection.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Connection.
        :type system_tags: dict(str, dict(str, object))

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Connection.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Connection.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this Connection.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Connection.
        :type time_updated: datetime

        :param vault_id:
            The value to assign to the vault_id property of this Connection.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this Connection.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this Connection.
        :type subnet_id: str

        :param ingress_ips:
            The value to assign to the ingress_ips property of this Connection.
        :type ingress_ips: list[oci.golden_gate.models.IngressIpDetails]

        :param nsg_ids:
            The value to assign to the nsg_ids property of this Connection.
        :type nsg_ids: list[str]

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
            'nsg_ids': 'list[str]'
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
            'nsg_ids': 'nsgIds'
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

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['connectionType']

        if type == 'KAFKA':
            return 'KafkaConnection'

        if type == 'POSTGRESQL':
            return 'PostgresqlConnection'

        if type == 'OCI_OBJECT_STORAGE':
            return 'OciObjectStorageConnection'

        if type == 'KAFKA_SCHEMA_REGISTRY':
            return 'KafkaSchemaRegistryConnection'

        if type == 'GOLDENGATE':
            return 'GoldenGateConnection'

        if type == 'MYSQL':
            return 'MysqlConnection'

        if type == 'ORACLE':
            return 'OracleConnection'

        if type == 'AZURE_DATA_LAKE_STORAGE':
            return 'AzureDataLakeStorageConnection'

        if type == 'AZURE_SYNAPSE_ANALYTICS':
            return 'AzureSynapseConnection'
        else:
            return 'Connection'

    @property
    def connection_type(self):
        """
        **[Required]** Gets the connection_type of this Connection.
        The connection type.

        Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The connection_type of this Connection.
        :rtype: str
        """
        return self._connection_type

    @connection_type.setter
    def connection_type(self, connection_type):
        """
        Sets the connection_type of this Connection.
        The connection type.


        :param connection_type: The connection_type of this Connection.
        :type: str
        """
        allowed_values = ["GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS"]
        if not value_allowed_none_or_none_sentinel(connection_type, allowed_values):
            connection_type = 'UNKNOWN_ENUM_VALUE'
        self._connection_type = connection_type

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Connection.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Connection.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Connection.
        The `OCID`__ of the connection being
        referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Connection.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Connection.
        An object's Display Name.


        :return: The display_name of this Connection.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Connection.
        An object's Display Name.


        :param display_name: The display_name of this Connection.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Connection.
        Metadata about this specific object.


        :return: The description of this Connection.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Connection.
        Metadata about this specific object.


        :param description: The description of this Connection.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Connection.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Connection.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Connection.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Connection.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Connection.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Connection.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Connection.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists
        for cross-compatibility only.

        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Connection.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Connection.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Connection.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Connection.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.

        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Connection.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Connection.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this Connection.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Connection.
        The system tags associated with this resource, if any. The system tags are set by Oracle
        Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more
        information, see `Resource Tags`__.

        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this Connection.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Connection.
        Possible lifecycle states for connection.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Connection.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Connection.
        Possible lifecycle states for connection.


        :param lifecycle_state: The lifecycle_state of this Connection.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Connection.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this Connection.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Connection.
        Describes the object's current state in detail. For example, it can be used to provide
        actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this Connection.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Connection.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this Connection.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Connection.
        The time the resource was created. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this Connection.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Connection.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Connection.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Connection.
        The time the resource was last updated. The format is defined by
        `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Connection.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def vault_id(self):
        """
        Gets the vault_id of this Connection.
        The `OCID`__ of the customer vault being
        referenced.
        If provided, this will reference a vault which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to manage secrets contained
        within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vault_id of this Connection.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this Connection.
        The `OCID`__ of the customer vault being
        referenced.
        If provided, this will reference a vault which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to manage secrets contained
        within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vault_id: The vault_id of this Connection.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def key_id(self):
        """
        Gets the key_id of this Connection.
        The `OCID`__ of the customer \"Master\" key being
        referenced.
        If provided, this will reference a key which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to utilize this key to
        manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_id of this Connection.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this Connection.
        The `OCID`__ of the customer \"Master\" key being
        referenced.
        If provided, this will reference a key which the customer will be required to ensure
        the policies are established to permit the GoldenGate Service to utilize this key to
        manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_id: The key_id of this Connection.
        :type: str
        """
        self._key_id = key_id

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this Connection.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this Connection.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Connection.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this Connection.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def ingress_ips(self):
        """
        Gets the ingress_ips of this Connection.
        List of ingress IP addresses, from where the GoldenGate deployment connects to this connection's privateIp.


        :return: The ingress_ips of this Connection.
        :rtype: list[oci.golden_gate.models.IngressIpDetails]
        """
        return self._ingress_ips

    @ingress_ips.setter
    def ingress_ips(self, ingress_ips):
        """
        Sets the ingress_ips of this Connection.
        List of ingress IP addresses, from where the GoldenGate deployment connects to this connection's privateIp.


        :param ingress_ips: The ingress_ips of this Connection.
        :type: list[oci.golden_gate.models.IngressIpDetails]
        """
        self._ingress_ips = ingress_ips

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this Connection.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :return: The nsg_ids of this Connection.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this Connection.
        An array of Network Security Group OCIDs used to define network access for either Deployments or Connections.


        :param nsg_ids: The nsg_ids of this Connection.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
