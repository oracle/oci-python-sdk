# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupVaultDetails(object):
    """
    BackupVaultDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupVaultDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param backup_location:
            The value to assign to the backup_location property of this BackupVaultDetails.
        :type backup_location: oci.key_management.models.BackupLocation

        :param is_include_keys:
            The value to assign to the is_include_keys property of this BackupVaultDetails.
        :type is_include_keys: bool

        """
        self.swagger_types = {
            'backup_location': 'BackupLocation',
            'is_include_keys': 'bool'
        }

        self.attribute_map = {
            'backup_location': 'backupLocation',
            'is_include_keys': 'isIncludeKeys'
        }

        self._backup_location = None
        self._is_include_keys = None

    @property
    def backup_location(self):
        """
        Gets the backup_location of this BackupVaultDetails.

        :return: The backup_location of this BackupVaultDetails.
        :rtype: oci.key_management.models.BackupLocation
        """
        return self._backup_location

    @backup_location.setter
    def backup_location(self, backup_location):
        """
        Sets the backup_location of this BackupVaultDetails.

        :param backup_location: The backup_location of this BackupVaultDetails.
        :type: oci.key_management.models.BackupLocation
        """
        self._backup_location = backup_location

    @property
    def is_include_keys(self):
        """
        Gets the is_include_keys of this BackupVaultDetails.

        :return: The is_include_keys of this BackupVaultDetails.
        :rtype: bool
        """
        return self._is_include_keys

    @is_include_keys.setter
    def is_include_keys(self, is_include_keys):
        """
        Sets the is_include_keys of this BackupVaultDetails.

        :param is_include_keys: The is_include_keys of this BackupVaultDetails.
        :type: bool
        """
        self._is_include_keys = is_include_keys

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
