# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompleteExternalBackupJobDetails(object):
    """
    CompleteExternalBackupJobDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompleteExternalBackupJobDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param tde_wallet_path:
            The value to assign to the tde_wallet_path property of this CompleteExternalBackupJobDetails.
        :type tde_wallet_path: str

        :param cf_backup_handle:
            The value to assign to the cf_backup_handle property of this CompleteExternalBackupJobDetails.
        :type cf_backup_handle: str

        :param spf_backup_handle:
            The value to assign to the spf_backup_handle property of this CompleteExternalBackupJobDetails.
        :type spf_backup_handle: str

        :param sql_patches:
            The value to assign to the sql_patches property of this CompleteExternalBackupJobDetails.
        :type sql_patches: list[str]

        :param data_size:
            The value to assign to the data_size property of this CompleteExternalBackupJobDetails.
        :type data_size: int

        :param redo_size:
            The value to assign to the redo_size property of this CompleteExternalBackupJobDetails.
        :type redo_size: int

        """
        self.swagger_types = {
            'tde_wallet_path': 'str',
            'cf_backup_handle': 'str',
            'spf_backup_handle': 'str',
            'sql_patches': 'list[str]',
            'data_size': 'int',
            'redo_size': 'int'
        }

        self.attribute_map = {
            'tde_wallet_path': 'tdeWalletPath',
            'cf_backup_handle': 'cfBackupHandle',
            'spf_backup_handle': 'spfBackupHandle',
            'sql_patches': 'sqlPatches',
            'data_size': 'dataSize',
            'redo_size': 'redoSize'
        }

        self._tde_wallet_path = None
        self._cf_backup_handle = None
        self._spf_backup_handle = None
        self._sql_patches = None
        self._data_size = None
        self._redo_size = None

    @property
    def tde_wallet_path(self):
        """
        Gets the tde_wallet_path of this CompleteExternalBackupJobDetails.
        If the database being backed up is TDE enabled, this will be the path to the associated TDE wallet in Object Storage.


        :return: The tde_wallet_path of this CompleteExternalBackupJobDetails.
        :rtype: str
        """
        return self._tde_wallet_path

    @tde_wallet_path.setter
    def tde_wallet_path(self, tde_wallet_path):
        """
        Sets the tde_wallet_path of this CompleteExternalBackupJobDetails.
        If the database being backed up is TDE enabled, this will be the path to the associated TDE wallet in Object Storage.


        :param tde_wallet_path: The tde_wallet_path of this CompleteExternalBackupJobDetails.
        :type: str
        """
        self._tde_wallet_path = tde_wallet_path

    @property
    def cf_backup_handle(self):
        """
        Gets the cf_backup_handle of this CompleteExternalBackupJobDetails.
        The handle of the control file backup.


        :return: The cf_backup_handle of this CompleteExternalBackupJobDetails.
        :rtype: str
        """
        return self._cf_backup_handle

    @cf_backup_handle.setter
    def cf_backup_handle(self, cf_backup_handle):
        """
        Sets the cf_backup_handle of this CompleteExternalBackupJobDetails.
        The handle of the control file backup.


        :param cf_backup_handle: The cf_backup_handle of this CompleteExternalBackupJobDetails.
        :type: str
        """
        self._cf_backup_handle = cf_backup_handle

    @property
    def spf_backup_handle(self):
        """
        Gets the spf_backup_handle of this CompleteExternalBackupJobDetails.
        The handle of the spfile backup.


        :return: The spf_backup_handle of this CompleteExternalBackupJobDetails.
        :rtype: str
        """
        return self._spf_backup_handle

    @spf_backup_handle.setter
    def spf_backup_handle(self, spf_backup_handle):
        """
        Sets the spf_backup_handle of this CompleteExternalBackupJobDetails.
        The handle of the spfile backup.


        :param spf_backup_handle: The spf_backup_handle of this CompleteExternalBackupJobDetails.
        :type: str
        """
        self._spf_backup_handle = spf_backup_handle

    @property
    def sql_patches(self):
        """
        Gets the sql_patches of this CompleteExternalBackupJobDetails.
        The list of SQL patches that need to be applied to the backup during the restore.


        :return: The sql_patches of this CompleteExternalBackupJobDetails.
        :rtype: list[str]
        """
        return self._sql_patches

    @sql_patches.setter
    def sql_patches(self, sql_patches):
        """
        Sets the sql_patches of this CompleteExternalBackupJobDetails.
        The list of SQL patches that need to be applied to the backup during the restore.


        :param sql_patches: The sql_patches of this CompleteExternalBackupJobDetails.
        :type: list[str]
        """
        self._sql_patches = sql_patches

    @property
    def data_size(self):
        """
        Gets the data_size of this CompleteExternalBackupJobDetails.
        The size of the data in the database, in megabytes.


        :return: The data_size of this CompleteExternalBackupJobDetails.
        :rtype: int
        """
        return self._data_size

    @data_size.setter
    def data_size(self, data_size):
        """
        Sets the data_size of this CompleteExternalBackupJobDetails.
        The size of the data in the database, in megabytes.


        :param data_size: The data_size of this CompleteExternalBackupJobDetails.
        :type: int
        """
        self._data_size = data_size

    @property
    def redo_size(self):
        """
        Gets the redo_size of this CompleteExternalBackupJobDetails.
        The size of the redo in the database, in megabytes.


        :return: The redo_size of this CompleteExternalBackupJobDetails.
        :rtype: int
        """
        return self._redo_size

    @redo_size.setter
    def redo_size(self, redo_size):
        """
        Sets the redo_size of this CompleteExternalBackupJobDetails.
        The size of the redo in the database, in megabytes.


        :param redo_size: The redo_size of this CompleteExternalBackupJobDetails.
        :type: int
        """
        self._redo_size = redo_size

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
