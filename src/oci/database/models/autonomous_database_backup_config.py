# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseBackupConfig(object):
    """
    Autonomous Database configuration details for storing `manual backups`__ in the `Object Storage`__ service.

    __ https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/backup-restore.html#GUID-9035DFB8-4702-4CEB-8281-C2A303820809
    __ https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm
    """

    #: A constant which can be used with the manual_backup_type property of a AutonomousDatabaseBackupConfig.
    #: This constant has a value of "NONE"
    MANUAL_BACKUP_TYPE_NONE = "NONE"

    #: A constant which can be used with the manual_backup_type property of a AutonomousDatabaseBackupConfig.
    #: This constant has a value of "OBJECT_STORE"
    MANUAL_BACKUP_TYPE_OBJECT_STORE = "OBJECT_STORE"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseBackupConfig object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param manual_backup_bucket_name:
            The value to assign to the manual_backup_bucket_name property of this AutonomousDatabaseBackupConfig.
        :type manual_backup_bucket_name: str

        :param manual_backup_type:
            The value to assign to the manual_backup_type property of this AutonomousDatabaseBackupConfig.
            Allowed values for this property are: "NONE", "OBJECT_STORE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type manual_backup_type: str

        """
        self.swagger_types = {
            'manual_backup_bucket_name': 'str',
            'manual_backup_type': 'str'
        }

        self.attribute_map = {
            'manual_backup_bucket_name': 'manualBackupBucketName',
            'manual_backup_type': 'manualBackupType'
        }

        self._manual_backup_bucket_name = None
        self._manual_backup_type = None

    @property
    def manual_backup_bucket_name(self):
        """
        Gets the manual_backup_bucket_name of this AutonomousDatabaseBackupConfig.
        Name of `Object Storage`__ bucket to use for storing manual backups.

        __ https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm


        :return: The manual_backup_bucket_name of this AutonomousDatabaseBackupConfig.
        :rtype: str
        """
        return self._manual_backup_bucket_name

    @manual_backup_bucket_name.setter
    def manual_backup_bucket_name(self, manual_backup_bucket_name):
        """
        Sets the manual_backup_bucket_name of this AutonomousDatabaseBackupConfig.
        Name of `Object Storage`__ bucket to use for storing manual backups.

        __ https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm


        :param manual_backup_bucket_name: The manual_backup_bucket_name of this AutonomousDatabaseBackupConfig.
        :type: str
        """
        self._manual_backup_bucket_name = manual_backup_bucket_name

    @property
    def manual_backup_type(self):
        """
        Gets the manual_backup_type of this AutonomousDatabaseBackupConfig.
        The manual backup destination type.

        Allowed values for this property are: "NONE", "OBJECT_STORE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The manual_backup_type of this AutonomousDatabaseBackupConfig.
        :rtype: str
        """
        return self._manual_backup_type

    @manual_backup_type.setter
    def manual_backup_type(self, manual_backup_type):
        """
        Sets the manual_backup_type of this AutonomousDatabaseBackupConfig.
        The manual backup destination type.


        :param manual_backup_type: The manual_backup_type of this AutonomousDatabaseBackupConfig.
        :type: str
        """
        allowed_values = ["NONE", "OBJECT_STORE"]
        if not value_allowed_none_or_none_sentinel(manual_backup_type, allowed_values):
            manual_backup_type = 'UNKNOWN_ENUM_VALUE'
        self._manual_backup_type = manual_backup_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
