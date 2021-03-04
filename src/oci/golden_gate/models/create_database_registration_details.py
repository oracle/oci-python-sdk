# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseRegistrationDetails(object):
    """
    The information about a new DatabaseRegistration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseRegistrationDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDatabaseRegistrationDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateDatabaseRegistrationDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDatabaseRegistrationDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDatabaseRegistrationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDatabaseRegistrationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param fqdn:
            The value to assign to the fqdn property of this CreateDatabaseRegistrationDetails.
        :type fqdn: str

        :param ip_address:
            The value to assign to the ip_address property of this CreateDatabaseRegistrationDetails.
        :type ip_address: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDatabaseRegistrationDetails.
        :type subnet_id: str

        :param database_id:
            The value to assign to the database_id property of this CreateDatabaseRegistrationDetails.
        :type database_id: str

        :param username:
            The value to assign to the username property of this CreateDatabaseRegistrationDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateDatabaseRegistrationDetails.
        :type password: str

        :param connection_string:
            The value to assign to the connection_string property of this CreateDatabaseRegistrationDetails.
        :type connection_string: str

        :param wallet:
            The value to assign to the wallet property of this CreateDatabaseRegistrationDetails.
        :type wallet: str

        :param alias_name:
            The value to assign to the alias_name property of this CreateDatabaseRegistrationDetails.
        :type alias_name: str

        :param vault_id:
            The value to assign to the vault_id property of this CreateDatabaseRegistrationDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateDatabaseRegistrationDetails.
        :type key_id: str

        :param secret_compartment_id:
            The value to assign to the secret_compartment_id property of this CreateDatabaseRegistrationDetails.
        :type secret_compartment_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'fqdn': 'str',
            'ip_address': 'str',
            'subnet_id': 'str',
            'database_id': 'str',
            'username': 'str',
            'password': 'str',
            'connection_string': 'str',
            'wallet': 'str',
            'alias_name': 'str',
            'vault_id': 'str',
            'key_id': 'str',
            'secret_compartment_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'fqdn': 'fqdn',
            'ip_address': 'ipAddress',
            'subnet_id': 'subnetId',
            'database_id': 'databaseId',
            'username': 'username',
            'password': 'password',
            'connection_string': 'connectionString',
            'wallet': 'wallet',
            'alias_name': 'aliasName',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'secret_compartment_id': 'secretCompartmentId'
        }

        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._fqdn = None
        self._ip_address = None
        self._subnet_id = None
        self._database_id = None
        self._username = None
        self._password = None
        self._connection_string = None
        self._wallet = None
        self._alias_name = None
        self._vault_id = None
        self._key_id = None
        self._secret_compartment_id = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDatabaseRegistrationDetails.
        An object's Display Name.


        :return: The display_name of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDatabaseRegistrationDetails.
        An object's Display Name.


        :param display_name: The display_name of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateDatabaseRegistrationDetails.
        Metadata about this specific object.


        :return: The description of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDatabaseRegistrationDetails.
        Metadata about this specific object.


        :param description: The description of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the compartment being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDatabaseRegistrationDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateDatabaseRegistrationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDatabaseRegistrationDetails.
        A simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateDatabaseRegistrationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDatabaseRegistrationDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateDatabaseRegistrationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDatabaseRegistrationDetails.
        Tags defined for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateDatabaseRegistrationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def fqdn(self):
        """
        **[Required]** Gets the fqdn of this CreateDatabaseRegistrationDetails.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :return: The fqdn of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._fqdn

    @fqdn.setter
    def fqdn(self, fqdn):
        """
        Sets the fqdn of this CreateDatabaseRegistrationDetails.
        A three-label Fully Qualified Domain Name (FQDN) for a resource.


        :param fqdn: The fqdn of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._fqdn = fqdn

    @property
    def ip_address(self):
        """
        Gets the ip_address of this CreateDatabaseRegistrationDetails.
        The private IP address in the customer's VCN of the customer's endpoint, typically a database.


        :return: The ip_address of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this CreateDatabaseRegistrationDetails.
        The private IP address in the customer's VCN of the customer's endpoint, typically a database.


        :param ip_address: The ip_address of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the subnet being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def database_id(self):
        """
        Gets the database_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_id of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._database_id

    @database_id.setter
    def database_id(self, database_id):
        """
        Sets the database_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the database being referenced.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_id: The database_id of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._database_id = database_id

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateDatabaseRegistrationDetails.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.


        :return: The username of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateDatabaseRegistrationDetails.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must already exist and be available for use by the database.  It must conform to the security requirements implemented by the database including length, case sensitivity, and so on.


        :param username: The username of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateDatabaseRegistrationDetails.
        The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.


        :return: The password of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateDatabaseRegistrationDetails.
        The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the specific security requirements implemented by the database including length, case sensitivity, and so on.


        :param password: The password of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._password = password

    @property
    def connection_string(self):
        """
        Gets the connection_string of this CreateDatabaseRegistrationDetails.
        Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.


        :return: The connection_string of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this CreateDatabaseRegistrationDetails.
        Connect descriptor or Easy Connect Naming method that Oracle GoldenGate uses to connect to a database.


        :param connection_string: The connection_string of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def wallet(self):
        """
        Gets the wallet of this CreateDatabaseRegistrationDetails.
        The wallet contents Oracle GoldenGate uses to make connections to a database.  This attribute is expected to be base64 encoded.


        :return: The wallet of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._wallet

    @wallet.setter
    def wallet(self, wallet):
        """
        Sets the wallet of this CreateDatabaseRegistrationDetails.
        The wallet contents Oracle GoldenGate uses to make connections to a database.  This attribute is expected to be base64 encoded.


        :param wallet: The wallet of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._wallet = wallet

    @property
    def alias_name(self):
        """
        **[Required]** Gets the alias_name of this CreateDatabaseRegistrationDetails.
        Credential store alias.


        :return: The alias_name of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """
        Sets the alias_name of this CreateDatabaseRegistrationDetails.
        Credential store alias.


        :param alias_name: The alias_name of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._alias_name = alias_name

    @property
    def vault_id(self):
        """
        Gets the vault_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vault_id of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the customer vault being referenced. If provided, this will reference a vault which the customer will be required to ensure the policies are established to permit the GoldenGate Service to manage secrets contained within this vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vault_id: The vault_id of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def key_id(self):
        """
        Gets the key_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_id of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """
        Sets the key_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the customer \"Master\" key being referenced. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this key to manage secrets.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_id: The key_id of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def secret_compartment_id(self):
        """
        Gets the secret_compartment_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the compartment where the the GGS Secret will be created. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this Compartment in which to create a Secret.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The secret_compartment_id of this CreateDatabaseRegistrationDetails.
        :rtype: str
        """
        return self._secret_compartment_id

    @secret_compartment_id.setter
    def secret_compartment_id(self, secret_compartment_id):
        """
        Sets the secret_compartment_id of this CreateDatabaseRegistrationDetails.
        The `OCID`__ of the compartment where the the GGS Secret will be created. If provided, this will reference a key which the customer will be required to ensure the policies are established to permit the GoldenGate Service to utilize this Compartment in which to create a Secret.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param secret_compartment_id: The secret_compartment_id of this CreateDatabaseRegistrationDetails.
        :type: str
        """
        self._secret_compartment_id = secret_compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
