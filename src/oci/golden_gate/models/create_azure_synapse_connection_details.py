# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAzureSynapseConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Azure Synapse Analytics Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAzureSynapseConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateAzureSynapseConnectionDetails.connection_type` attribute
        of this class is ``AZURE_SYNAPSE_ANALYTICS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateAzureSynapseConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateAzureSynapseConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateAzureSynapseConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAzureSynapseConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAzureSynapseConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAzureSynapseConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this CreateAzureSynapseConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateAzureSynapseConnectionDetails.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateAzureSynapseConnectionDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateAzureSynapseConnectionDetails.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this CreateAzureSynapseConnectionDetails.
        :type technology_type: str

        :param connection_string:
            The value to assign to the connection_string property of this CreateAzureSynapseConnectionDetails.
        :type connection_string: str

        :param username:
            The value to assign to the username property of this CreateAzureSynapseConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateAzureSynapseConnectionDetails.
        :type password: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'connection_string': 'str',
            'username': 'str',
            'password': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'connection_string': 'connectionString',
            'username': 'username',
            'password': 'password'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._nsg_ids = None
        self._technology_type = None
        self._connection_string = None
        self._username = None
        self._password = None
        self._connection_type = 'AZURE_SYNAPSE_ANALYTICS'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateAzureSynapseConnectionDetails.
        The Azure Synapse Analytics technology type.


        :return: The technology_type of this CreateAzureSynapseConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateAzureSynapseConnectionDetails.
        The Azure Synapse Analytics technology type.


        :param technology_type: The technology_type of this CreateAzureSynapseConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def connection_string(self):
        """
        **[Required]** Gets the connection_string of this CreateAzureSynapseConnectionDetails.
        JDBC connection string.
        e.g.: 'jdbc:sqlserver://<synapse-workspace>.sql.azuresynapse.net:1433;database=<db-name>;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'


        :return: The connection_string of this CreateAzureSynapseConnectionDetails.
        :rtype: str
        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        """
        Sets the connection_string of this CreateAzureSynapseConnectionDetails.
        JDBC connection string.
        e.g.: 'jdbc:sqlserver://<synapse-workspace>.sql.azuresynapse.net:1433;database=<db-name>;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=300;'


        :param connection_string: The connection_string of this CreateAzureSynapseConnectionDetails.
        :type: str
        """
        self._connection_string = connection_string

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateAzureSynapseConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must
        already exist and be available for use by the database.  It must conform to the security
        requirements implemented by the database including length, case sensitivity, and so on.


        :return: The username of this CreateAzureSynapseConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateAzureSynapseConnectionDetails.
        The username Oracle GoldenGate uses to connect the associated RDBMS.  This username must
        already exist and be available for use by the database.  It must conform to the security
        requirements implemented by the database including length, case sensitivity, and so on.


        :param username: The username of this CreateAzureSynapseConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateAzureSynapseConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the
        specific security requirements implemented by the database including length, case
        sensitivity, and so on.


        :return: The password of this CreateAzureSynapseConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateAzureSynapseConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated RDBMS.  It must conform to the
        specific security requirements implemented by the database including length, case
        sensitivity, and so on.


        :param password: The password of this CreateAzureSynapseConnectionDetails.
        :type: str
        """
        self._password = password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
