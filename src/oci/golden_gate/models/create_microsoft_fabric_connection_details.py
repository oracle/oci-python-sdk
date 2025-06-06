# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMicrosoftFabricConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Microsoft Fabric Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMicrosoftFabricConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateMicrosoftFabricConnectionDetails.connection_type` attribute
        of this class is ``MICROSOFT_FABRIC`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateMicrosoftFabricConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateMicrosoftFabricConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateMicrosoftFabricConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMicrosoftFabricConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMicrosoftFabricConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMicrosoftFabricConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param locks:
            The value to assign to the locks property of this CreateMicrosoftFabricConnectionDetails.
        :type locks: list[oci.golden_gate.models.AddResourceLockDetails]

        :param vault_id:
            The value to assign to the vault_id property of this CreateMicrosoftFabricConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateMicrosoftFabricConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateMicrosoftFabricConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateMicrosoftFabricConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this CreateMicrosoftFabricConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this CreateMicrosoftFabricConnectionDetails.
        :type does_use_secret_ids: bool

        :param technology_type:
            The value to assign to the technology_type property of this CreateMicrosoftFabricConnectionDetails.
        :type technology_type: str

        :param tenant_id:
            The value to assign to the tenant_id property of this CreateMicrosoftFabricConnectionDetails.
        :type tenant_id: str

        :param client_id:
            The value to assign to the client_id property of this CreateMicrosoftFabricConnectionDetails.
        :type client_id: str

        :param client_secret:
            The value to assign to the client_secret property of this CreateMicrosoftFabricConnectionDetails.
        :type client_secret: str

        :param client_secret_secret_id:
            The value to assign to the client_secret_secret_id property of this CreateMicrosoftFabricConnectionDetails.
        :type client_secret_secret_id: str

        :param endpoint:
            The value to assign to the endpoint property of this CreateMicrosoftFabricConnectionDetails.
        :type endpoint: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'locks': 'list[AddResourceLockDetails]',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'technology_type': 'str',
            'tenant_id': 'str',
            'client_id': 'str',
            'client_secret': 'str',
            'client_secret_secret_id': 'str',
            'endpoint': 'str'
        }
        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'locks': 'locks',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'technology_type': 'technologyType',
            'tenant_id': 'tenantId',
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'client_secret_secret_id': 'clientSecretSecretId',
            'endpoint': 'endpoint'
        }
        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._locks = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._technology_type = None
        self._tenant_id = None
        self._client_id = None
        self._client_secret = None
        self._client_secret_secret_id = None
        self._endpoint = None
        self._connection_type = 'MICROSOFT_FABRIC'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateMicrosoftFabricConnectionDetails.
        The Microsoft Fabric technology type.


        :return: The technology_type of this CreateMicrosoftFabricConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateMicrosoftFabricConnectionDetails.
        The Microsoft Fabric technology type.


        :param technology_type: The technology_type of this CreateMicrosoftFabricConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def tenant_id(self):
        """
        **[Required]** Gets the tenant_id of this CreateMicrosoftFabricConnectionDetails.
        Azure tenant ID of the application.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :return: The tenant_id of this CreateMicrosoftFabricConnectionDetails.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """
        Sets the tenant_id of this CreateMicrosoftFabricConnectionDetails.
        Azure tenant ID of the application.
        e.g.: 14593954-d337-4a61-a364-9f758c64f97f


        :param tenant_id: The tenant_id of this CreateMicrosoftFabricConnectionDetails.
        :type: str
        """
        self._tenant_id = tenant_id

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this CreateMicrosoftFabricConnectionDetails.
        Azure client ID of the application.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :return: The client_id of this CreateMicrosoftFabricConnectionDetails.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CreateMicrosoftFabricConnectionDetails.
        Azure client ID of the application.
        e.g.: 06ecaabf-8b80-4ec8-a0ec-20cbf463703d


        :param client_id: The client_id of this CreateMicrosoftFabricConnectionDetails.
        :type: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        """
        Gets the client_secret of this CreateMicrosoftFabricConnectionDetails.
        Client secret associated with the client id.
        Deprecated: This field is deprecated and replaced by \"clientSecretSecretId\". This field will be removed after February 15 2026.


        :return: The client_secret of this CreateMicrosoftFabricConnectionDetails.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this CreateMicrosoftFabricConnectionDetails.
        Client secret associated with the client id.
        Deprecated: This field is deprecated and replaced by \"clientSecretSecretId\". This field will be removed after February 15 2026.


        :param client_secret: The client_secret of this CreateMicrosoftFabricConnectionDetails.
        :type: str
        """
        self._client_secret = client_secret

    @property
    def client_secret_secret_id(self):
        """
        Gets the client_secret_secret_id of this CreateMicrosoftFabricConnectionDetails.
        The `OCID`__ of the Secret where the client secret is stored.
        Note: When provided, 'clientSecret' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The client_secret_secret_id of this CreateMicrosoftFabricConnectionDetails.
        :rtype: str
        """
        return self._client_secret_secret_id

    @client_secret_secret_id.setter
    def client_secret_secret_id(self, client_secret_secret_id):
        """
        Sets the client_secret_secret_id of this CreateMicrosoftFabricConnectionDetails.
        The `OCID`__ of the Secret where the client secret is stored.
        Note: When provided, 'clientSecret' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param client_secret_secret_id: The client_secret_secret_id of this CreateMicrosoftFabricConnectionDetails.
        :type: str
        """
        self._client_secret_secret_id = client_secret_secret_id

    @property
    def endpoint(self):
        """
        Gets the endpoint of this CreateMicrosoftFabricConnectionDetails.
        Optional Microsoft Fabric service endpoint.
        Default value: https://onelake.dfs.fabric.microsoft.com


        :return: The endpoint of this CreateMicrosoftFabricConnectionDetails.
        :rtype: str
        """
        return self._endpoint

    @endpoint.setter
    def endpoint(self, endpoint):
        """
        Sets the endpoint of this CreateMicrosoftFabricConnectionDetails.
        Optional Microsoft Fabric service endpoint.
        Default value: https://onelake.dfs.fabric.microsoft.com


        :param endpoint: The endpoint of this CreateMicrosoftFabricConnectionDetails.
        :type: str
        """
        self._endpoint = endpoint

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
