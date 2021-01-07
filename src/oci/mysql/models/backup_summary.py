# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class BackupSummary(object):
    """
    Details of Backups such as OCID, description, backupType, and so on.

    To use any of the API operations, you must be authorized in an IAM
    policy. If you're not authorized, talk to an administrator. If you're an
    administrator who needs to write policies to give users access, see
    `Getting Started with Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new BackupSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this BackupSummary.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this BackupSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this BackupSummary.
        :type description: str

        :param time_created:
            The value to assign to the time_created property of this BackupSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this BackupSummary.
        :type lifecycle_state: str

        :param backup_type:
            The value to assign to the backup_type property of this BackupSummary.
        :type backup_type: str

        :param creation_type:
            The value to assign to the creation_type property of this BackupSummary.
        :type creation_type: str

        :param db_system_id:
            The value to assign to the db_system_id property of this BackupSummary.
        :type db_system_id: str

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this BackupSummary.
        :type data_storage_size_in_gbs: int

        :param backup_size_in_gbs:
            The value to assign to the backup_size_in_gbs property of this BackupSummary.
        :type backup_size_in_gbs: int

        :param retention_in_days:
            The value to assign to the retention_in_days property of this BackupSummary.
        :type retention_in_days: int

        :param mysql_version:
            The value to assign to the mysql_version property of this BackupSummary.
        :type mysql_version: str

        :param shape_name:
            The value to assign to the shape_name property of this BackupSummary.
        :type shape_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this BackupSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this BackupSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'backup_type': 'str',
            'creation_type': 'str',
            'db_system_id': 'str',
            'data_storage_size_in_gbs': 'int',
            'backup_size_in_gbs': 'int',
            'retention_in_days': 'int',
            'mysql_version': 'str',
            'shape_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'backup_type': 'backupType',
            'creation_type': 'creationType',
            'db_system_id': 'dbSystemId',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'backup_size_in_gbs': 'backupSizeInGBs',
            'retention_in_days': 'retentionInDays',
            'mysql_version': 'mysqlVersion',
            'shape_name': 'shapeName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._time_created = None
        self._lifecycle_state = None
        self._backup_type = None
        self._creation_type = None
        self._db_system_id = None
        self._data_storage_size_in_gbs = None
        self._backup_size_in_gbs = None
        self._retention_in_days = None
        self._mysql_version = None
        self._shape_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this BackupSummary.
        OCID of the backup.


        :return: The id of this BackupSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this BackupSummary.
        OCID of the backup.


        :param id: The id of this BackupSummary.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this BackupSummary.
        A user-supplied display name for the backup.


        :return: The display_name of this BackupSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this BackupSummary.
        A user-supplied display name for the backup.


        :param display_name: The display_name of this BackupSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this BackupSummary.
        A user-supplied description of the backup.


        :return: The description of this BackupSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this BackupSummary.
        A user-supplied description of the backup.


        :param description: The description of this BackupSummary.
        :type: str
        """
        self._description = description

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this BackupSummary.
        The time the backup was created.


        :return: The time_created of this BackupSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this BackupSummary.
        The time the backup was created.


        :param time_created: The time_created of this BackupSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this BackupSummary.
        The state of the backup.


        :return: The lifecycle_state of this BackupSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this BackupSummary.
        The state of the backup.


        :param lifecycle_state: The lifecycle_state of this BackupSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def backup_type(self):
        """
        **[Required]** Gets the backup_type of this BackupSummary.
        The type of backup.


        :return: The backup_type of this BackupSummary.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this BackupSummary.
        The type of backup.


        :param backup_type: The backup_type of this BackupSummary.
        :type: str
        """
        self._backup_type = backup_type

    @property
    def creation_type(self):
        """
        **[Required]** Gets the creation_type of this BackupSummary.
        If the backup was created automatically, or by a manual request.


        :return: The creation_type of this BackupSummary.
        :rtype: str
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """
        Sets the creation_type of this BackupSummary.
        If the backup was created automatically, or by a manual request.


        :param creation_type: The creation_type of this BackupSummary.
        :type: str
        """
        self._creation_type = creation_type

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this BackupSummary.
        The OCID of the DB System the Backup is associated with.


        :return: The db_system_id of this BackupSummary.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this BackupSummary.
        The OCID of the DB System the Backup is associated with.


        :param db_system_id: The db_system_id of this BackupSummary.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this BackupSummary.
        Size of the data volume in GiBs.


        :return: The data_storage_size_in_gbs of this BackupSummary.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this BackupSummary.
        Size of the data volume in GiBs.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this BackupSummary.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def backup_size_in_gbs(self):
        """
        Gets the backup_size_in_gbs of this BackupSummary.
        The size of the backup in GiBs.


        :return: The backup_size_in_gbs of this BackupSummary.
        :rtype: int
        """
        return self._backup_size_in_gbs

    @backup_size_in_gbs.setter
    def backup_size_in_gbs(self, backup_size_in_gbs):
        """
        Sets the backup_size_in_gbs of this BackupSummary.
        The size of the backup in GiBs.


        :param backup_size_in_gbs: The backup_size_in_gbs of this BackupSummary.
        :type: int
        """
        self._backup_size_in_gbs = backup_size_in_gbs

    @property
    def retention_in_days(self):
        """
        Gets the retention_in_days of this BackupSummary.
        Number of days to retain this backup.


        :return: The retention_in_days of this BackupSummary.
        :rtype: int
        """
        return self._retention_in_days

    @retention_in_days.setter
    def retention_in_days(self, retention_in_days):
        """
        Sets the retention_in_days of this BackupSummary.
        Number of days to retain this backup.


        :param retention_in_days: The retention_in_days of this BackupSummary.
        :type: int
        """
        self._retention_in_days = retention_in_days

    @property
    def mysql_version(self):
        """
        Gets the mysql_version of this BackupSummary.
        The version of the DB System used for backup.


        :return: The mysql_version of this BackupSummary.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this BackupSummary.
        The version of the DB System used for backup.


        :param mysql_version: The mysql_version of this BackupSummary.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def shape_name(self):
        """
        Gets the shape_name of this BackupSummary.
        The shape of the DB System instance used for backup.


        :return: The shape_name of this BackupSummary.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this BackupSummary.
        The shape of the DB System instance used for backup.


        :param shape_name: The shape_name of this BackupSummary.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this BackupSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this BackupSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this BackupSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this BackupSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this BackupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this BackupSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this BackupSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this BackupSummary.
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
