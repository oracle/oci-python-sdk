# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_db_system_source_details import CreateDbSystemSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbSystemSourceFromBackupDetails(CreateDbSystemSourceDetails):
    """
    Use the backupId to specify from which backup the new DB System will be created.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbSystemSourceFromBackupDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.mysql.models.CreateDbSystemSourceFromBackupDetails.source_type` attribute
        of this class is ``BACKUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this CreateDbSystemSourceFromBackupDetails.
            Allowed values for this property are: "NONE", "BACKUP", "IMPORTURL"
        :type source_type: str

        :param backup_id:
            The value to assign to the backup_id property of this CreateDbSystemSourceFromBackupDetails.
        :type backup_id: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'backup_id': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'backup_id': 'backupId'
        }

        self._source_type = None
        self._backup_id = None
        self._source_type = 'BACKUP'

    @property
    def backup_id(self):
        """
        **[Required]** Gets the backup_id of this CreateDbSystemSourceFromBackupDetails.
        The OCID of the backup to be used as the source for the new DB System.


        :return: The backup_id of this CreateDbSystemSourceFromBackupDetails.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """
        Sets the backup_id of this CreateDbSystemSourceFromBackupDetails.
        The OCID of the backup to be used as the source for the new DB System.


        :param backup_id: The backup_id of this CreateDbSystemSourceFromBackupDetails.
        :type: str
        """
        self._backup_id = backup_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
