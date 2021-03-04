# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseRegistration(object):
    """
    Represents the metadata description of a database used by deployments in the same compartment.
    """

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistration.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistration.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistration.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistration.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistration.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistration.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseRegistration.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseRegistration object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this DatabaseRegistration.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this DatabaseRegistration.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DatabaseRegistration.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseRegistration.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this DatabaseRegistration.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseRegistration.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseRegistration.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseRegistration.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseRegistration.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseRegistration.
        :type defined_tags: dict(str, dict(str, object))

        :param fqdn:
            The value to assign to the fqdn property of this DatabaseRegistration.
        :type fqdn: str

        :param ip_address:
            The value to assign to the ip_address property of this DatabaseRegistration.
        :type ip_address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DatabaseRegistration.
        :type subnet_id: str

        :param database_id:
            The value to assign to the database_id property of this DatabaseRegistration.
        :type database_id: str

        :param rce_private_ip:
            The value to assign to the rce_private_ip property of this DatabaseRegistration.
        :type rce_private_ip: str

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseRegistration.
        :type system_tags: dict(str, dict(str, object))

        :param username:
            The value to assign to the username property of this DatabaseRegistration.
        :type username: str

        :param connection_string:
            The value to assign to the connection_string property of this DatabaseRegistration.
        :type connection_string: str

        :param alias_name:
            The value to assign to the alias_name property of this DatabaseRegistration.
        :type alias_name: str

        :param vault_id:
            The value to assign to the vault_id property of this DatabaseRegistration.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this DatabaseRegistration.
        :type key_id: str

        :param secret_compartment_id:
            The value to assign to the secret_compartment_id property of this DatabaseRegistration.
        :type secret_compartment_id: str

        :param secret_id:
            The value to assign to the secret_id property of this DatabaseRegistration.
        :type secret_id: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'fqdn': 'str',
            'ip_address': 'str',
            'subnet_id': 'str',
            'database_id': 'str',
            'rce_private_ip': 'str',
            'system_tags': 'dict(str, dict(str, object))',
            'username': 'str',
            'connection_string': 'str',
            'alias_name': 'str',
            'vault_id': 'str',
            'key_id': 'str',
            'secret_compartment_id': 'str',
            'secret_id': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'fqdn': 'fqdn',
            'ip_address': 'ipAddress',
            'subnet_id': 'subnetId',
            'database_id': 'databaseId',
            'rce_private_ip': 'rcePrivateIp',
            'system_tags': 'systemTags',
            'username': 'username',
            'connection_string': 'connectionString',
            'alias_name': 'aliasName',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'secret_compartment_id': 'secretCompartmentId',
            'secret_id': 'secretId'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._fqdn = None
        self._ip_address = None
        self._subnet_id = None
        self._database_id = None
        self._rce_private_ip = None
        self._system_tags = None
        self._username = None
        self._connection_string = None
        self._alias_name = None
        self._vault_id = None
        self._key_id = None
        self._secret_compartment_id = None
        self._secret_id = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatabaseRegistration.
        The `OCID`__ of the databaseRegistration being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DatabaseRegistration.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseRegistration.
        The `OCID`__ of the databaseRegistration being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DatabaseRegistration.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this DatabaseRegistration.
        An object's Display Name.


        :return: The display_name of this DatabaseRegistration.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DatabaseRegistration.
        An object's Display Name.


        :param display_name: The display_name of this DatabaseRegistration.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DatabaseRegistration.
        Metadata about this specific object.


        :return: The description of this DatabaseRegistration.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatabaseRegistration.
        Metadata about this specific object.


        :param description: The description of this DatabaseRegistration.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DatabaseRegistration.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DatabaseRegistration.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseRegistration.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DatabaseRegistration.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this DatabaseRegistration.
        The time the resource was created. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this DatabaseRegistration.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatabaseRegistration.
        The time the resource was created. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this DatabaseRegistration.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this DatabaseRegistration.
        The time the resource was last updated. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this DatabaseRegistration.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DatabaseRegistration.
        The time the resource was last updated. The format is defined by `RFC3339`__, such as `2016-08-25T21:10:29.600Z`.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this DatabaseRegistration.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this DatabaseRegistration.
        Possible lifecycle states.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseRegistration.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseRegistration.
        Possible lifecycle states.


        :param lifecycle_state: The lifecycle_state of this DatabaseRegistration.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseRegistration.
        Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this DatabaseRegistration.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseRegistration.
        Describes the object's current state in detail. For example, it can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this DatabaseRegistration.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DatabaseRegistration.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatabaseRegistration.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseRegistration.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatabaseRegistration.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DatabaseRegistration.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatabaseRegistration.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseRegistration.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatabaseRegistration.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def fqdn(self):
        """
        **[Required]** Gets the fqdn of this DatabaseRegistration.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :return: The fqdn of this DatabaseRegistration.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this DatabaseRegistration.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :param fqdn: The fqdn of this DatabaseRegistration.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this DatabaseRegistration.
        The private IP address in the customer's VCN of the customer's endpoint, typically a database.


        :return: The ip_address of this DatabaseRegistration.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this DatabaseRegistration.
        The private IP address in the customer's VCN of the customer's endpoint, typically a database.


        :param ip_address: The ip_address of this DatabaseRegistration.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this DatabaseRegistration.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this DatabaseRegistration.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DatabaseRegistration.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DatabaseRegistration.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def database_id(self):
        """
        Gets the database_id of this DatabaseRegistration.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this DatabaseRegistration.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this DatabaseRegistration.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this DatabaseRegistration.
        :type: str
        """
        self._database_id = database_id

    @property
    def rce_private_ip(self):
        """
        Gets the rce_private_ip of this DatabaseRegistration.
        A Private Endpoint IP Address created in the customer's subnet.  A customer database can expect network traffic initiated by GGS from this IP address and send network traffic to this IP address, typically in response to requests from GGS (OGG).  The customer may utilize this IP address in Security Lists or Network Security Groups (NSG) as needed.


        :return: The rce_private_ip of this DatabaseRegistration.
        :rtype: str
        """
        return self._rce_private_ip

    @rce_private_ip.setter
    def rce_private_ip(self, rce_private_ip):
        """
        Sets the rce_private_ip of this DatabaseRegistration.
        A Private Endpoint IP Address created in the customer's subnet.  A customer database can expect network traffic initiated by GGS from this IP address and send network traffic to this IP address, typically in response to requests from GGS (OGG).  The customer may utilize this IP address in Security Lists or Network Security Groups (NSG) as needed.


        :param rce_private_ip: The rce_private_ip of this DatabaseRegistration.
        :type: str
        """
        self._rce_private_ip = rce_private_ip

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DatabaseRegistration.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this DatabaseRegistration.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DatabaseRegistration.
        The system tags associated with this resource, if any. The system tags are set by Oracle Cloud Infrastructure services. Each key is predefined and scoped to namespaces.  For more information, see `Resource Tags`__.
        Example: `{orcl-cloud: {free-tier-retain: true}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this DatabaseRegistration.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def username(self):
        """
        **[Required]** Gets the username of this DatabaseRegistration.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.


        :return: The username of this DatabaseRegistration.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this DatabaseRegistration.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.


        :param username: The username of this DatabaseRegistration.
        :type: str
        """
        self._username = username

    @property
    def connection_string(self):
        """
        Gets the connection_string of this DatabaseRegistration.
        Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.


        :return: The connection_string of this DatabaseRegistration.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this DatabaseRegistration.
        Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.


        :param connection_string: The connection_string of this DatabaseRegistration.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def alias_name(self):
        """
        **[Required]** Gets the alias_name of this DatabaseRegistration.
        Credential store alias.


        :return: The alias_name of this DatabaseRegistration.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """
        Sets the alias_name of this DatabaseRegistration.
        Credential store alias.


        :param alias_name: The alias_name of this DatabaseRegistration.
        :type: str
        """
        self._alias_name = alias_name

    @property
    def vault_id(self):
        """
        Gets the vault_id of this DatabaseRegistration.
        The `OCID`__ of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vault_id of this DatabaseRegistration.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this DatabaseRegistration.
        The `OCID`__ of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vault_id: The vault_id of this DatabaseRegistration.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def key_id(self):
        """
        Gets the key_id of this DatabaseRegistration.
        The `OCID`__ of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_id of this DatabaseRegistration.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this DatabaseRegistration.
        The `OCID`__ of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_id: The key_id of this DatabaseRegistration.
        :type: str
        """
        self._key_id = key_id

    @property
    def secret_compartment_id(self):
        """
        Gets the secret_compartment_id of this DatabaseRegistration.
        The `OCID`__ of the compartment where the the GGS Secret will be created. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this Compartment in which to create a Secret.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The secret_compartment_id of this DatabaseRegistration.
        :rtype: str
        """
        return self._secret_compartment_id

    @secret_compartment_id.setter
    def secret_compartment_id(self, secret_compartment_id):
        """
        Sets the secret_compartment_id of this DatabaseRegistration.
        The `OCID`__ of the compartment where the the GGS Secret will be created. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this Compartment in which to create a Secret.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param secret_compartment_id: The secret_compartment_id of this DatabaseRegistration.
        :type: str
        """
        self._secret_compartment_id = secret_compartment_id

    @property
    def secret_id(self):
        """
        Gets the secret_id of this DatabaseRegistration.
        The `OCID`__ of the customer GGS Secret being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this Secret

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The secret_id of this DatabaseRegistration.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this DatabaseRegistration.
        The `OCID`__ of the customer GGS Secret being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this Secret

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param secret_id: The secret_id of this DatabaseRegistration.
        :type: str
        """
        self._secret_id = secret_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
