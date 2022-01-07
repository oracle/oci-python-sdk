# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Backup(object):
    """
    A full or incremental copy of a DB System which can be used to create a
    new DB System or recover a DB System.

    To use any of the API operations, you must be authorized in an IAM
    policy. If you're not authorized, talk to an administrator. If you're an
    administrator who needs to write policies to give users access, see
    `Getting Started with
    Policies`__.

    __ https://docs.cloud.oracle.com/Content/Identity/Concepts/policygetstarted.htm
    """

    #: A constant which can be used with the lifecycle_state property of a Backup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Backup.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Backup.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Backup.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Backup.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Backup.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Backup.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the backup_type property of a Backup.
    #: This constant has a value of "FULL"
    BACKUP_TYPE_FULL = "FULL"

    #: A constant which can be used with the backup_type property of a Backup.
    #: This constant has a value of "INCREMENTAL"
    BACKUP_TYPE_INCREMENTAL = "INCREMENTAL"

    #: A constant which can be used with the creation_type property of a Backup.
    #: This constant has a value of "MANUAL"
    CREATION_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the creation_type property of a Backup.
    #: This constant has a value of "AUTOMATIC"
    CREATION_TYPE_AUTOMATIC = "AUTOMATIC"

    #: A constant which can be used with the creation_type property of a Backup.
    #: This constant has a value of "OPERATOR"
    CREATION_TYPE_OPERATOR = "OPERATOR"

    def __init__(self, **kwargs):
        """
        Initializes a new Backup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Backup.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Backup.
        :type display_name: str

        :param description:
            The value to assign to the description property of this Backup.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Backup.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this Backup.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Backup.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Backup.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Backup.
        :type lifecycle_details: str

        :param backup_type:
            The value to assign to the backup_type property of this Backup.
            Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_type: str

        :param creation_type:
            The value to assign to the creation_type property of this Backup.
            Allowed values for this property are: "MANUAL", "AUTOMATIC", "OPERATOR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type creation_type: str

        :param db_system_id:
            The value to assign to the db_system_id property of this Backup.
        :type db_system_id: str

        :param db_system_snapshot:
            The value to assign to the db_system_snapshot property of this Backup.
        :type db_system_snapshot: oci.mysql.models.DbSystemSnapshot

        :param backup_size_in_gbs:
            The value to assign to the backup_size_in_gbs property of this Backup.
        :type backup_size_in_gbs: int

        :param retention_in_days:
            The value to assign to the retention_in_days property of this Backup.
        :type retention_in_days: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this Backup.
        :type data_storage_size_in_gbs: int

        :param mysql_version:
            The value to assign to the mysql_version property of this Backup.
        :type mysql_version: str

        :param shape_name:
            The value to assign to the shape_name property of this Backup.
        :type shape_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Backup.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Backup.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'backup_type': 'str',
            'creation_type': 'str',
            'db_system_id': 'str',
            'db_system_snapshot': 'DbSystemSnapshot',
            'backup_size_in_gbs': 'int',
            'retention_in_days': 'int',
            'data_storage_size_in_gbs': 'int',
            'mysql_version': 'str',
            'shape_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'backup_type': 'backupType',
            'creation_type': 'creationType',
            'db_system_id': 'dbSystemId',
            'db_system_snapshot': 'dbSystemSnapshot',
            'backup_size_in_gbs': 'backupSizeInGBs',
            'retention_in_days': 'retentionInDays',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'mysql_version': 'mysqlVersion',
            'shape_name': 'shapeName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._backup_type = None
        self._creation_type = None
        self._db_system_id = None
        self._db_system_snapshot = None
        self._backup_size_in_gbs = None
        self._retention_in_days = None
        self._data_storage_size_in_gbs = None
        self._mysql_version = None
        self._shape_name = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Backup.
        OCID of the backup itself


        :return: The id of this Backup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Backup.
        OCID of the backup itself


        :param id: The id of this Backup.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this Backup.
        A user-supplied display name for the backup.


        :return: The display_name of this Backup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Backup.
        A user-supplied display name for the backup.


        :param display_name: The display_name of this Backup.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this Backup.
        A user-supplied description for the backup.


        :return: The description of this Backup.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Backup.
        A user-supplied description for the backup.


        :param description: The description of this Backup.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Backup.
        The OCID of the compartment.


        :return: The compartment_id of this Backup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Backup.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this Backup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Backup.
        The time the backup record was created.


        :return: The time_created of this Backup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Backup.
        The time the backup record was created.


        :param time_created: The time_created of this Backup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this Backup.
        The time at which the backup was updated.


        :return: The time_updated of this Backup.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Backup.
        The time at which the backup was updated.


        :param time_updated: The time_updated of this Backup.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Backup.
        The state of the backup.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Backup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Backup.
        The state of the backup.


        :param lifecycle_state: The lifecycle_state of this Backup.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        **[Required]** Gets the lifecycle_details of this Backup.
        Additional information about the current lifecycleState.


        :return: The lifecycle_details of this Backup.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Backup.
        Additional information about the current lifecycleState.


        :param lifecycle_details: The lifecycle_details of this Backup.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def backup_type(self):
        """
        **[Required]** Gets the backup_type of this Backup.
        The type of backup.

        Allowed values for this property are: "FULL", "INCREMENTAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_type of this Backup.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this Backup.
        The type of backup.


        :param backup_type: The backup_type of this Backup.
        :type: str
        """
        allowed_values = ["FULL", "INCREMENTAL"]
        if not value_allowed_none_or_none_sentinel(backup_type, allowed_values):
            backup_type = 'UNKNOWN_ENUM_VALUE'
        self._backup_type = backup_type

    @property
    def creation_type(self):
        """
        **[Required]** Gets the creation_type of this Backup.
        Indicates how the backup was created: manually, automatic, or by an Operator.

        Allowed values for this property are: "MANUAL", "AUTOMATIC", "OPERATOR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The creation_type of this Backup.
        :rtype: str
        """
        return self._creation_type

    @creation_type.setter
    def creation_type(self, creation_type):
        """
        Sets the creation_type of this Backup.
        Indicates how the backup was created: manually, automatic, or by an Operator.


        :param creation_type: The creation_type of this Backup.
        :type: str
        """
        allowed_values = ["MANUAL", "AUTOMATIC", "OPERATOR"]
        if not value_allowed_none_or_none_sentinel(creation_type, allowed_values):
            creation_type = 'UNKNOWN_ENUM_VALUE'
        self._creation_type = creation_type

    @property
    def db_system_id(self):
        """
        **[Required]** Gets the db_system_id of this Backup.
        The OCID of the DB System the backup is associated with.


        :return: The db_system_id of this Backup.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this Backup.
        The OCID of the DB System the backup is associated with.


        :param db_system_id: The db_system_id of this Backup.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def db_system_snapshot(self):
        """
        Gets the db_system_snapshot of this Backup.

        :return: The db_system_snapshot of this Backup.
        :rtype: oci.mysql.models.DbSystemSnapshot
        """
        return self._db_system_snapshot

    @db_system_snapshot.setter
    def db_system_snapshot(self, db_system_snapshot):
        """
        Sets the db_system_snapshot of this Backup.

        :param db_system_snapshot: The db_system_snapshot of this Backup.
        :type: oci.mysql.models.DbSystemSnapshot
        """
        self._db_system_snapshot = db_system_snapshot

    @property
    def backup_size_in_gbs(self):
        """
        Gets the backup_size_in_gbs of this Backup.
        The size of the backup in base-2 (IEC) gibibytes. (GiB).


        :return: The backup_size_in_gbs of this Backup.
        :rtype: int
        """
        return self._backup_size_in_gbs

    @backup_size_in_gbs.setter
    def backup_size_in_gbs(self, backup_size_in_gbs):
        """
        Sets the backup_size_in_gbs of this Backup.
        The size of the backup in base-2 (IEC) gibibytes. (GiB).


        :param backup_size_in_gbs: The backup_size_in_gbs of this Backup.
        :type: int
        """
        self._backup_size_in_gbs = backup_size_in_gbs

    @property
    def retention_in_days(self):
        """
        Gets the retention_in_days of this Backup.
        Number of days to retain this backup.


        :return: The retention_in_days of this Backup.
        :rtype: int
        """
        return self._retention_in_days

    @retention_in_days.setter
    def retention_in_days(self, retention_in_days):
        """
        Sets the retention_in_days of this Backup.
        Number of days to retain this backup.


        :param retention_in_days: The retention_in_days of this Backup.
        :type: int
        """
        self._retention_in_days = retention_in_days

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this Backup.
        Initial size of the data volume in GiBs.


        :return: The data_storage_size_in_gbs of this Backup.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this Backup.
        Initial size of the data volume in GiBs.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this Backup.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def mysql_version(self):
        """
        Gets the mysql_version of this Backup.
        The MySQL server version of the DB System used for backup.


        :return: The mysql_version of this Backup.
        :rtype: str
        """
        return self._mysql_version

    @mysql_version.setter
    def mysql_version(self, mysql_version):
        """
        Sets the mysql_version of this Backup.
        The MySQL server version of the DB System used for backup.


        :param mysql_version: The mysql_version of this Backup.
        :type: str
        """
        self._mysql_version = mysql_version

    @property
    def shape_name(self):
        """
        Gets the shape_name of this Backup.
        The shape of the DB System used for backup.


        :return: The shape_name of this Backup.
        :rtype: str
        """
        return self._shape_name

    @shape_name.setter
    def shape_name(self, shape_name):
        """
        Sets the shape_name of this Backup.
        The shape of the DB System used for backup.


        :param shape_name: The shape_name of this Backup.
        :type: str
        """
        self._shape_name = shape_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Backup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Backup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Backup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Backup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Backup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Backup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Backup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Backup.
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
