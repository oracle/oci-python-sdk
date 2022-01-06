# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .key_store_type_details import KeyStoreTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyStoreTypeFromOracleKeyVaultDetails(KeyStoreTypeDetails):
    """
    Details for Oracle Key Vault
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyStoreTypeFromOracleKeyVaultDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.KeyStoreTypeFromOracleKeyVaultDetails.type` attribute
        of this class is ``ORACLE_KEY_VAULT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this KeyStoreTypeFromOracleKeyVaultDetails.
            Allowed values for this property are: "ORACLE_KEY_VAULT"
        :type type: str

        :param connection_ips:
            The value to assign to the connection_ips property of this KeyStoreTypeFromOracleKeyVaultDetails.
        :type connection_ips: list[str]

        :param admin_username:
            The value to assign to the admin_username property of this KeyStoreTypeFromOracleKeyVaultDetails.
        :type admin_username: str

        :param vault_id:
            The value to assign to the vault_id property of this KeyStoreTypeFromOracleKeyVaultDetails.
        :type vault_id: str

        :param secret_id:
            The value to assign to the secret_id property of this KeyStoreTypeFromOracleKeyVaultDetails.
        :type secret_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'connection_ips': 'list[str]',
            'admin_username': 'str',
            'vault_id': 'str',
            'secret_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'connection_ips': 'connectionIps',
            'admin_username': 'adminUsername',
            'vault_id': 'vaultId',
            'secret_id': 'secretId'
        }

        self._type = None
        self._connection_ips = None
        self._admin_username = None
        self._vault_id = None
        self._secret_id = None
        self._type = 'ORACLE_KEY_VAULT'

    @property
    def connection_ips(self):
        """
        **[Required]** Gets the connection_ips of this KeyStoreTypeFromOracleKeyVaultDetails.
        The list of Oracle Key Vault connection IP addresses.


        :return: The connection_ips of this KeyStoreTypeFromOracleKeyVaultDetails.
        :rtype: list[str]
        """
        return self._connection_ips

    @connection_ips.setter
    def connection_ips(self, connection_ips):
        """
        Sets the connection_ips of this KeyStoreTypeFromOracleKeyVaultDetails.
        The list of Oracle Key Vault connection IP addresses.


        :param connection_ips: The connection_ips of this KeyStoreTypeFromOracleKeyVaultDetails.
        :type: list[str]
        """
        self._connection_ips = connection_ips

    @property
    def admin_username(self):
        """
        **[Required]** Gets the admin_username of this KeyStoreTypeFromOracleKeyVaultDetails.
        The administrator username to connect to Oracle Key Vault


        :return: The admin_username of this KeyStoreTypeFromOracleKeyVaultDetails.
        :rtype: str
        """
        return self._admin_username

    @admin_username.setter
    def admin_username(self, admin_username):
        """
        Sets the admin_username of this KeyStoreTypeFromOracleKeyVaultDetails.
        The administrator username to connect to Oracle Key Vault


        :param admin_username: The admin_username of this KeyStoreTypeFromOracleKeyVaultDetails.
        :type: str
        """
        self._admin_username = admin_username

    @property
    def vault_id(self):
        """
        **[Required]** Gets the vault_id of this KeyStoreTypeFromOracleKeyVaultDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this KeyStoreTypeFromOracleKeyVaultDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this KeyStoreTypeFromOracleKeyVaultDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this KeyStoreTypeFromOracleKeyVaultDetails.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def secret_id(self):
        """
        **[Required]** Gets the secret_id of this KeyStoreTypeFromOracleKeyVaultDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The secret_id of this KeyStoreTypeFromOracleKeyVaultDetails.
        :rtype: str
        """
        return self._secret_id

    @secret_id.setter
    def secret_id(self, secret_id):
        """
        Sets the secret_id of this KeyStoreTypeFromOracleKeyVaultDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `secret`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param secret_id: The secret_id of this KeyStoreTypeFromOracleKeyVaultDetails.
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
