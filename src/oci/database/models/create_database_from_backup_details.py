# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDatabaseFromBackupDetails(object):
    """
    CreateDatabaseFromBackupDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDatabaseFromBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param admin_password:
            The value to assign to the admin_password property of this CreateDatabaseFromBackupDetails.
        :type admin_password: str

        :param backup_id:
            The value to assign to the backup_id property of this CreateDatabaseFromBackupDetails.
        :type backup_id: str

        :param backup_tde_password:
            The value to assign to the backup_tde_password property of this CreateDatabaseFromBackupDetails.
        :type backup_tde_password: str

        """
        self.swagger_types = {
            'admin_password': 'str',
            'backup_id': 'str',
            'backup_tde_password': 'str'
        }

        self.attribute_map = {
            'admin_password': 'adminPassword',
            'backup_id': 'backupId',
            'backup_tde_password': 'backupTDEPassword'
        }

        self._admin_password = None
        self._backup_id = None
        self._backup_tde_password = None

    @property
    def admin_password(self):
        """
        **[Required]** Gets the admin_password of this CreateDatabaseFromBackupDetails.
        A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :return: The admin_password of this CreateDatabaseFromBackupDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateDatabaseFromBackupDetails.
        A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, \\#, or -.


        :param admin_password: The admin_password of this CreateDatabaseFromBackupDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def backup_id(self):
        """
        **[Required]** Gets the backup_id of this CreateDatabaseFromBackupDetails.
        The backup `OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The backup_id of this CreateDatabaseFromBackupDetails.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """
        Sets the backup_id of this CreateDatabaseFromBackupDetails.
        The backup `OCID`__.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param backup_id: The backup_id of this CreateDatabaseFromBackupDetails.
        :type: str
        """
        self._backup_id = backup_id

    @property
    def backup_tde_password(self):
        """
        **[Required]** Gets the backup_tde_password of this CreateDatabaseFromBackupDetails.
        The password to open the TDE wallet.


        :return: The backup_tde_password of this CreateDatabaseFromBackupDetails.
        :rtype: str
        """
        return self._backup_tde_password

    @backup_tde_password.setter
    def backup_tde_password(self, backup_tde_password):
        """
        Sets the backup_tde_password of this CreateDatabaseFromBackupDetails.
        The password to open the TDE wallet.


        :param backup_tde_password: The backup_tde_password of this CreateDatabaseFromBackupDetails.
        :type: str
        """
        self._backup_tde_password = backup_tde_password

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
