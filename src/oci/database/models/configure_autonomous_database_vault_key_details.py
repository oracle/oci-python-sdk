# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConfigureAutonomousDatabaseVaultKeyDetails(object):
    """
    Configuration details for the Autonomous Database `vault`__ key.

    __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ConfigureAutonomousDatabaseVaultKeyDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kms_key_id:
            The value to assign to the kms_key_id property of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :type kms_key_id: str

        :param vault_id:
            The value to assign to the vault_id property of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :type vault_id: str

        :param is_using_oracle_managed_keys:
            The value to assign to the is_using_oracle_managed_keys property of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :type is_using_oracle_managed_keys: bool

        """
        self.swagger_types = {
            'kms_key_id': 'str',
            'vault_id': 'str',
            'is_using_oracle_managed_keys': 'bool'
        }

        self.attribute_map = {
            'kms_key_id': 'kmsKeyId',
            'vault_id': 'vaultId',
            'is_using_oracle_managed_keys': 'isUsingOracleManagedKeys'
        }

        self._kms_key_id = None
        self._vault_id = None
        self._is_using_oracle_managed_keys = None

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def is_using_oracle_managed_keys(self):
        """
        Gets the is_using_oracle_managed_keys of this ConfigureAutonomousDatabaseVaultKeyDetails.
        True if disable Customer Managed Keys and use Oracle Managed Keys.


        :return: The is_using_oracle_managed_keys of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :rtype: bool
        """
        return self._is_using_oracle_managed_keys

    @is_using_oracle_managed_keys.setter
    def is_using_oracle_managed_keys(self, is_using_oracle_managed_keys):
        """
        Sets the is_using_oracle_managed_keys of this ConfigureAutonomousDatabaseVaultKeyDetails.
        True if disable Customer Managed Keys and use Oracle Managed Keys.


        :param is_using_oracle_managed_keys: The is_using_oracle_managed_keys of this ConfigureAutonomousDatabaseVaultKeyDetails.
        :type: bool
        """
        self._is_using_oracle_managed_keys = is_using_oracle_managed_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
