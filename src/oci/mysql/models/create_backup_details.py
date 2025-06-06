# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190415


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateBackupDetails(object):
    """
    Complete information for a Backup.
    """

    #: A constant which can be used with the soft_delete property of a CreateBackupDetails.
    #: This constant has a value of "ENABLED"
    SOFT_DELETE_ENABLED = "ENABLED"

    #: A constant which can be used with the soft_delete property of a CreateBackupDetails.
    #: This constant has a value of "DISABLED"
    SOFT_DELETE_DISABLED = "DISABLED"

    #: A constant which can be used with the backup_type property of a CreateBackupDetails.
    #: This constant has a value of "FULL"
    BACKUP_TYPE_FULL = "FULL"

    #: A constant which can be used with the backup_type property of a CreateBackupDetails.
    #: This constant has a value of "INCREMENTAL"
    BACKUP_TYPE_INCREMENTAL = "INCREMENTAL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateBackupDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateBackupDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateBackupDetails.
        :type description: str

        :param soft_delete:
            The value to assign to the soft_delete property of this CreateBackupDetails.
            Allowed values for this property are: "ENABLED", "DISABLED"
        :type soft_delete: str

        :param backup_type:
            The value to assign to the backup_type property of this CreateBackupDetails.
            Allowed values for this property are: "FULL", "INCREMENTAL"
        :type backup_type: str

        :param db_system_id:
            The value to assign to the db_system_id property of this CreateBackupDetails.
        :type db_system_id: str

        :param retention_in_days:
            The value to assign to the retention_in_days property of this CreateBackupDetails.
        :type retention_in_days: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateBackupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'description': 'str',
            'soft_delete': 'str',
            'backup_type': 'str',
            'db_system_id': 'str',
            'retention_in_days': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }
        self.attribute_map = {
            'display_name': 'displayName',
            'description': 'description',
            'soft_delete': 'softDelete',
            'backup_type': 'backupType',
            'db_system_id': 'dbSystemId',
            'retention_in_days': 'retentionInDays',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }
        self._display_name = None
        self._description = None
        self._soft_delete = None
        self._backup_type = None
        self._db_system_id = None
        self._retention_in_days = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateBackupDetails.
        A user-supplied display name for the backup.


        :return: The display_name of this CreateBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateBackupDetails.
        A user-supplied display name for the backup.


        :param display_name: The display_name of this CreateBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this CreateBackupDetails.
        A user-supplied description for the backup.


        :return: The description of this CreateBackupDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateBackupDetails.
        A user-supplied description for the backup.


        :param description: The description of this CreateBackupDetails.
        :type: str
        """
        self._description = description

    @property
    def soft_delete(self):
        """
        Gets the soft_delete of this CreateBackupDetails.
        Retains the backup to be deleted due to the retention policy in DELETE SCHEDULED
        state for 7 days before permanently deleting it.

        Allowed values for this property are: "ENABLED", "DISABLED"


        :return: The soft_delete of this CreateBackupDetails.
        :rtype: str
        """
        return self._soft_delete

    @soft_delete.setter
    def soft_delete(self, soft_delete):
        """
        Sets the soft_delete of this CreateBackupDetails.
        Retains the backup to be deleted due to the retention policy in DELETE SCHEDULED
        state for 7 days before permanently deleting it.


        :param soft_delete: The soft_delete of this CreateBackupDetails.
        :type: str
        """
        allowed_values = ["ENABLED", "DISABLED"]
        if not value_allowed_none_or_none_sentinel(soft_delete, allowed_values):
            raise ValueError(
                f"Invalid value for `soft_delete`, must be None or one of {allowed_values}"
            )
        self._soft_delete = soft_delete

    @property
    def backup_type(self):
        """
        Gets the backup_type of this CreateBackupDetails.
        The type of backup.

        Allowed values for this property are: "FULL", "INCREMENTAL"


        :return: The backup_type of this CreateBackupDetails.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this CreateBackupDetails.
        The type of backup.


        :param backup_type: The backup_type of this CreateBackupDetails.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(backup_type, allowed_values):
            raise ValueError(
                f"Invalid value for `backup_type`, must be None or one of {allowed_values}"
            )
        self._backup_type = backup_type

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this CreateBackupDetails.
        The OCID of the DB System the Backup is associated with.


        :return: The db_system_id of this CreateBackupDetails.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this CreateBackupDetails.
        The OCID of the DB System the Backup is associated with.


        :param db_system_id: The db_system_id of this CreateBackupDetails.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def retention_in_days(self):
        """
        Gets the retention_in_days of this CreateBackupDetails.
        Number of days to retain this backup.


        :return: The retention_in_days of this CreateBackupDetails.
        :rtype: int
        """
        return self._retention_in_days

    @retention_in_days.setter
    def retention_in_days(self, retention_in_days):
        """
        Sets the retention_in_days of this CreateBackupDetails.
        Number of days to retain this backup.


        :param retention_in_days: The retention_in_days of this CreateBackupDetails.
        :type: int
        """
        self._retention_in_days = retention_in_days

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateBackupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateBackupDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateBackupDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateBackupDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateBackupDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateBackupDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateBackupDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
