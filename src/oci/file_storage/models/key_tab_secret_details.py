# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20171215


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class KeyTabSecretDetails(object):
    """
    Secret details of keytabs in Vault.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new KeyTabSecretDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_tab_secret_id:
            The value to assign to the key_tab_secret_id property of this KeyTabSecretDetails.
        :type key_tab_secret_id: str

        :param current_key_tab_secret_version:
            The value to assign to the current_key_tab_secret_version property of this KeyTabSecretDetails.
        :type current_key_tab_secret_version: int

        :param backup_key_tab_secret_version:
            The value to assign to the backup_key_tab_secret_version property of this KeyTabSecretDetails.
        :type backup_key_tab_secret_version: int

        """
        self.swagger_types = {
            'key_tab_secret_id': 'str',
            'current_key_tab_secret_version': 'int',
            'backup_key_tab_secret_version': 'int'
        }
        self.attribute_map = {
            'key_tab_secret_id': 'keyTabSecretId',
            'current_key_tab_secret_version': 'currentKeyTabSecretVersion',
            'backup_key_tab_secret_version': 'backupKeyTabSecretVersion'
        }
        self._key_tab_secret_id = None
        self._current_key_tab_secret_version = None
        self._backup_key_tab_secret_version = None

    @property
    def key_tab_secret_id(self):
        """
        **[Required]** Gets the key_tab_secret_id of this KeyTabSecretDetails.
        The `OCID`__ of the keytab secret in the Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_tab_secret_id of this KeyTabSecretDetails.
        :rtype: str
        """
        return self._key_tab_secret_id

    @key_tab_secret_id.setter
    def key_tab_secret_id(self, key_tab_secret_id):
        """
        Sets the key_tab_secret_id of this KeyTabSecretDetails.
        The `OCID`__ of the keytab secret in the Vault.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_tab_secret_id: The key_tab_secret_id of this KeyTabSecretDetails.
        :type: str
        """
        self._key_tab_secret_id = key_tab_secret_id

    @property
    def current_key_tab_secret_version(self):
        """
        **[Required]** Gets the current_key_tab_secret_version of this KeyTabSecretDetails.
        Version of the keytab secret in the Vault to use.


        :return: The current_key_tab_secret_version of this KeyTabSecretDetails.
        :rtype: int
        """
        return self._current_key_tab_secret_version

    @current_key_tab_secret_version.setter
    def current_key_tab_secret_version(self, current_key_tab_secret_version):
        """
        Sets the current_key_tab_secret_version of this KeyTabSecretDetails.
        Version of the keytab secret in the Vault to use.


        :param current_key_tab_secret_version: The current_key_tab_secret_version of this KeyTabSecretDetails.
        :type: int
        """
        self._current_key_tab_secret_version = current_key_tab_secret_version

    @property
    def backup_key_tab_secret_version(self):
        """
        Gets the backup_key_tab_secret_version of this KeyTabSecretDetails.
        Version of the keytab secret in the Vault to use as a backup.


        :return: The backup_key_tab_secret_version of this KeyTabSecretDetails.
        :rtype: int
        """
        return self._backup_key_tab_secret_version

    @backup_key_tab_secret_version.setter
    def backup_key_tab_secret_version(self, backup_key_tab_secret_version):
        """
        Sets the backup_key_tab_secret_version of this KeyTabSecretDetails.
        Version of the keytab secret in the Vault to use as a backup.


        :param backup_key_tab_secret_version: The backup_key_tab_secret_version of this KeyTabSecretDetails.
        :type: int
        """
        self._backup_key_tab_secret_version = backup_key_tab_secret_version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
