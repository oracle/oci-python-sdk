# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200407

from .update_connection_details import UpdateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOracleNosqlConnectionDetails(UpdateConnectionDetails):
    """
    The information to update a Oracle NoSQL Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOracleNosqlConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.UpdateOracleNosqlConnectionDetails.connection_type` attribute
        of this class is ``ORACLE_NOSQL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this UpdateOracleNosqlConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB", "AMAZON_KINESIS", "AMAZON_REDSHIFT", "DB2", "REDIS", "ELASTICSEARCH", "GENERIC", "GOOGLE_CLOUD_STORAGE", "GOOGLE_BIGQUERY", "DATABRICKS", "GOOGLE_PUBSUB", "MICROSOFT_FABRIC", "ICEBERG"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOracleNosqlConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateOracleNosqlConnectionDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOracleNosqlConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOracleNosqlConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this UpdateOracleNosqlConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this UpdateOracleNosqlConnectionDetails.
        :type key_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateOracleNosqlConnectionDetails.
        :type nsg_ids: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateOracleNosqlConnectionDetails.
        :type subnet_id: str

        :param routing_method:
            The value to assign to the routing_method property of this UpdateOracleNosqlConnectionDetails.
            Allowed values for this property are: "SHARED_SERVICE_ENDPOINT", "SHARED_DEPLOYMENT_ENDPOINT", "DEDICATED_ENDPOINT"
        :type routing_method: str

        :param does_use_secret_ids:
            The value to assign to the does_use_secret_ids property of this UpdateOracleNosqlConnectionDetails.
        :type does_use_secret_ids: bool

        :param tenancy_id:
            The value to assign to the tenancy_id property of this UpdateOracleNosqlConnectionDetails.
        :type tenancy_id: str

        :param region:
            The value to assign to the region property of this UpdateOracleNosqlConnectionDetails.
        :type region: str

        :param user_id:
            The value to assign to the user_id property of this UpdateOracleNosqlConnectionDetails.
        :type user_id: str

        :param private_key_file:
            The value to assign to the private_key_file property of this UpdateOracleNosqlConnectionDetails.
        :type private_key_file: str

        :param private_key_file_secret_id:
            The value to assign to the private_key_file_secret_id property of this UpdateOracleNosqlConnectionDetails.
        :type private_key_file_secret_id: str

        :param private_key_passphrase:
            The value to assign to the private_key_passphrase property of this UpdateOracleNosqlConnectionDetails.
        :type private_key_passphrase: str

        :param private_key_passphrase_secret_id:
            The value to assign to the private_key_passphrase_secret_id property of this UpdateOracleNosqlConnectionDetails.
        :type private_key_passphrase_secret_id: str

        :param public_key_fingerprint:
            The value to assign to the public_key_fingerprint property of this UpdateOracleNosqlConnectionDetails.
        :type public_key_fingerprint: str

        :param should_use_resource_principal:
            The value to assign to the should_use_resource_principal property of this UpdateOracleNosqlConnectionDetails.
        :type should_use_resource_principal: bool

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'nsg_ids': 'list[str]',
            'subnet_id': 'str',
            'routing_method': 'str',
            'does_use_secret_ids': 'bool',
            'tenancy_id': 'str',
            'region': 'str',
            'user_id': 'str',
            'private_key_file': 'str',
            'private_key_file_secret_id': 'str',
            'private_key_passphrase': 'str',
            'private_key_passphrase_secret_id': 'str',
            'public_key_fingerprint': 'str',
            'should_use_resource_principal': 'bool'
        }
        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'nsg_ids': 'nsgIds',
            'subnet_id': 'subnetId',
            'routing_method': 'routingMethod',
            'does_use_secret_ids': 'doesUseSecretIds',
            'tenancy_id': 'tenancyId',
            'region': 'region',
            'user_id': 'userId',
            'private_key_file': 'privateKeyFile',
            'private_key_file_secret_id': 'privateKeyFileSecretId',
            'private_key_passphrase': 'privateKeyPassphrase',
            'private_key_passphrase_secret_id': 'privateKeyPassphraseSecretId',
            'public_key_fingerprint': 'publicKeyFingerprint',
            'should_use_resource_principal': 'shouldUseResourcePrincipal'
        }
        self._connection_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._nsg_ids = None
        self._subnet_id = None
        self._routing_method = None
        self._does_use_secret_ids = None
        self._tenancy_id = None
        self._region = None
        self._user_id = None
        self._private_key_file = None
        self._private_key_file_secret_id = None
        self._private_key_passphrase = None
        self._private_key_passphrase_secret_id = None
        self._public_key_fingerprint = None
        self._should_use_resource_principal = None
        self._connection_type = 'ORACLE_NOSQL'

    @property
    def tenancy_id(self):
        """
        Gets the tenancy_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the related OCI tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The tenancy_id of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._tenancy_id

    @tenancy_id.setter
    def tenancy_id(self, tenancy_id):
        """
        Sets the tenancy_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the related OCI tenancy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param tenancy_id: The tenancy_id of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._tenancy_id = tenancy_id

    @property
    def region(self):
        """
        Gets the region of this UpdateOracleNosqlConnectionDetails.
        The name of the region. e.g.: us-ashburn-1
        If the region is not provided, backend will default to the default region.


        :return: The region of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """
        Sets the region of this UpdateOracleNosqlConnectionDetails.
        The name of the region. e.g.: us-ashburn-1
        If the region is not provided, backend will default to the default region.


        :param region: The region of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._region = region

    @property
    def user_id(self):
        """
        Gets the user_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the OCI user who will access the Oracle NoSQL database.
        The user must have write access to the table they want to connect to.
        If the user is not provided, backend will default to the user who is calling the API endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The user_id of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the OCI user who will access the Oracle NoSQL database.
        The user must have write access to the table they want to connect to.
        If the user is not provided, backend will default to the user who is calling the API endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param user_id: The user_id of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._user_id = user_id

    @property
    def private_key_file(self):
        """
        Gets the private_key_file of this UpdateOracleNosqlConnectionDetails.
        The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm
        Deprecated: This field is deprecated and replaced by \"privateKeyFileSecretId\". This field will be removed after February 15 2026.


        :return: The private_key_file of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_file

    @private_key_file.setter
    def private_key_file(self, private_key_file):
        """
        Sets the private_key_file of this UpdateOracleNosqlConnectionDetails.
        The base64 encoded content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm
        Deprecated: This field is deprecated and replaced by \"privateKeyFileSecretId\". This field will be removed after February 15 2026.


        :param private_key_file: The private_key_file of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_file = private_key_file

    @property
    def private_key_file_secret_id(self):
        """
        Gets the private_key_file_secret_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm
        Note: When provided, 'privateKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_key_file_secret_id of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_file_secret_id

    @private_key_file_secret_id.setter
    def private_key_file_secret_id(self, private_key_file_secret_id):
        """
        Sets the private_key_file_secret_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the content of the private key file (PEM file) corresponding to the API key of the fingerprint.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm
        Note: When provided, 'privateKeyFile' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_key_file_secret_id: The private_key_file_secret_id of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_file_secret_id = private_key_file_secret_id

    @property
    def private_key_passphrase(self):
        """
        Gets the private_key_passphrase of this UpdateOracleNosqlConnectionDetails.
        The passphrase of the private key.
        Deprecated: This field is deprecated and replaced by \"privateKeyPassphraseSecretId\". This field will be removed after February 15 2026.


        :return: The private_key_passphrase of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_passphrase

    @private_key_passphrase.setter
    def private_key_passphrase(self, private_key_passphrase):
        """
        Sets the private_key_passphrase of this UpdateOracleNosqlConnectionDetails.
        The passphrase of the private key.
        Deprecated: This field is deprecated and replaced by \"privateKeyPassphraseSecretId\". This field will be removed after February 15 2026.


        :param private_key_passphrase: The private_key_passphrase of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_passphrase = private_key_passphrase

    @property
    def private_key_passphrase_secret_id(self):
        """
        Gets the private_key_passphrase_secret_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the passphrase of the private key.
        Note: When provided, 'privateKeyPassphrase' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_key_passphrase_secret_id of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._private_key_passphrase_secret_id

    @private_key_passphrase_secret_id.setter
    def private_key_passphrase_secret_id(self, private_key_passphrase_secret_id):
        """
        Sets the private_key_passphrase_secret_id of this UpdateOracleNosqlConnectionDetails.
        The `OCID`__ of the Secret that stores the passphrase of the private key.
        Note: When provided, 'privateKeyPassphrase' field must not be provided.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_key_passphrase_secret_id: The private_key_passphrase_secret_id of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._private_key_passphrase_secret_id = private_key_passphrase_secret_id

    @property
    def public_key_fingerprint(self):
        """
        Gets the public_key_fingerprint of this UpdateOracleNosqlConnectionDetails.
        The fingerprint of the API Key of the user specified by the userId.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :return: The public_key_fingerprint of this UpdateOracleNosqlConnectionDetails.
        :rtype: str
        """
        return self._public_key_fingerprint

    @public_key_fingerprint.setter
    def public_key_fingerprint(self, public_key_fingerprint):
        """
        Sets the public_key_fingerprint of this UpdateOracleNosqlConnectionDetails.
        The fingerprint of the API Key of the user specified by the userId.
        See documentation: https://docs.oracle.com/en-us/iaas/Content/Identity/Tasks/managingcredentials.htm


        :param public_key_fingerprint: The public_key_fingerprint of this UpdateOracleNosqlConnectionDetails.
        :type: str
        """
        self._public_key_fingerprint = public_key_fingerprint

    @property
    def should_use_resource_principal(self):
        """
        Gets the should_use_resource_principal of this UpdateOracleNosqlConnectionDetails.
        Indicates that the user intents to connect to the instance through resource principal.


        :return: The should_use_resource_principal of this UpdateOracleNosqlConnectionDetails.
        :rtype: bool
        """
        return self._should_use_resource_principal

    @should_use_resource_principal.setter
    def should_use_resource_principal(self, should_use_resource_principal):
        """
        Sets the should_use_resource_principal of this UpdateOracleNosqlConnectionDetails.
        Indicates that the user intents to connect to the instance through resource principal.


        :param should_use_resource_principal: The should_use_resource_principal of this UpdateOracleNosqlConnectionDetails.
        :type: bool
        """
        self._should_use_resource_principal = should_use_resource_principal

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
