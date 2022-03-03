# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Database(object):
    """
    Database model.
    """

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "UPGRADING"
    LIFECYCLE_STATE_UPGRADING = "UPGRADING"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "CONVERTING"
    LIFECYCLE_STATE_CONVERTING = "CONVERTING"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "RESTORE_FAILED"
    LIFECYCLE_STATE_RESTORE_FAILED = "RESTORE_FAILED"

    #: A constant which can be used with the lifecycle_state property of a Database.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Database object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Database.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Database.
        :type compartment_id: str

        :param character_set:
            The value to assign to the character_set property of this Database.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this Database.
        :type ncharacter_set: str

        :param db_home_id:
            The value to assign to the db_home_id property of this Database.
        :type db_home_id: str

        :param db_system_id:
            The value to assign to the db_system_id property of this Database.
        :type db_system_id: str

        :param vm_cluster_id:
            The value to assign to the vm_cluster_id property of this Database.
        :type vm_cluster_id: str

        :param db_name:
            The value to assign to the db_name property of this Database.
        :type db_name: str

        :param pdb_name:
            The value to assign to the pdb_name property of this Database.
        :type pdb_name: str

        :param db_workload:
            The value to assign to the db_workload property of this Database.
        :type db_workload: str

        :param db_unique_name:
            The value to assign to the db_unique_name property of this Database.
        :type db_unique_name: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Database.
        :type lifecycle_details: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Database.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "UPGRADING", "CONVERTING", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this Database.
        :type time_created: datetime

        :param last_backup_timestamp:
            The value to assign to the last_backup_timestamp property of this Database.
        :type last_backup_timestamp: datetime

        :param db_backup_config:
            The value to assign to the db_backup_config property of this Database.
        :type db_backup_config: oci.database.models.DbBackupConfig

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Database.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Database.
        :type defined_tags: dict(str, dict(str, object))

        :param connection_strings:
            The value to assign to the connection_strings property of this Database.
        :type connection_strings: oci.database.models.DatabaseConnectionStrings

        :param kms_key_id:
            The value to assign to the kms_key_id property of this Database.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this Database.
        :type kms_key_version_id: str

        :param vault_id:
            The value to assign to the vault_id property of this Database.
        :type vault_id: str

        :param source_database_point_in_time_recovery_timestamp:
            The value to assign to the source_database_point_in_time_recovery_timestamp property of this Database.
        :type source_database_point_in_time_recovery_timestamp: datetime

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this Database.
        :type database_software_image_id: str

        :param is_cdb:
            The value to assign to the is_cdb property of this Database.
        :type is_cdb: bool

        :param database_management_config:
            The value to assign to the database_management_config property of this Database.
        :type database_management_config: oci.database.models.CloudDatabaseManagementConfig

        :param sid_prefix:
            The value to assign to the sid_prefix property of this Database.
        :type sid_prefix: str

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'db_home_id': 'str',
            'db_system_id': 'str',
            'vm_cluster_id': 'str',
            'db_name': 'str',
            'pdb_name': 'str',
            'db_workload': 'str',
            'db_unique_name': 'str',
            'lifecycle_details': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'last_backup_timestamp': 'datetime',
            'db_backup_config': 'DbBackupConfig',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'connection_strings': 'DatabaseConnectionStrings',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'vault_id': 'str',
            'source_database_point_in_time_recovery_timestamp': 'datetime',
            'database_software_image_id': 'str',
            'is_cdb': 'bool',
            'database_management_config': 'CloudDatabaseManagementConfig',
            'sid_prefix': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'db_home_id': 'dbHomeId',
            'db_system_id': 'dbSystemId',
            'vm_cluster_id': 'vmClusterId',
            'db_name': 'dbName',
            'pdb_name': 'pdbName',
            'db_workload': 'dbWorkload',
            'db_unique_name': 'dbUniqueName',
            'lifecycle_details': 'lifecycleDetails',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'last_backup_timestamp': 'lastBackupTimestamp',
            'db_backup_config': 'dbBackupConfig',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'connection_strings': 'connectionStrings',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'vault_id': 'vaultId',
            'source_database_point_in_time_recovery_timestamp': 'sourceDatabasePointInTimeRecoveryTimestamp',
            'database_software_image_id': 'databaseSoftwareImageId',
            'is_cdb': 'isCdb',
            'database_management_config': 'databaseManagementConfig',
            'sid_prefix': 'sidPrefix'
        }

        self._id = None
        self._compartment_id = None
        self._character_set = None
        self._ncharacter_set = None
        self._db_home_id = None
        self._db_system_id = None
        self._vm_cluster_id = None
        self._db_name = None
        self._pdb_name = None
        self._db_workload = None
        self._db_unique_name = None
        self._lifecycle_details = None
        self._lifecycle_state = None
        self._time_created = None
        self._last_backup_timestamp = None
        self._db_backup_config = None
        self._freeform_tags = None
        self._defined_tags = None
        self._connection_strings = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._vault_id = None
        self._source_database_point_in_time_recovery_timestamp = None
        self._database_software_image_id = None
        self._is_cdb = None
        self._database_management_config = None
        self._sid_prefix = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Database.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this Database.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Database.
        The `OCID`__ of the database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this Database.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Database.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this Database.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Database.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this Database.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def character_set(self):
        """
        Gets the character_set of this Database.
        The character set for the database.


        :return: The character_set of this Database.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this Database.
        The character set for the database.


        :param character_set: The character_set of this Database.
        :type: str
        """
        self._character_set = character_set

    @property
    def ncharacter_set(self):
        """
        Gets the ncharacter_set of this Database.
        The national character set for the database.


        :return: The ncharacter_set of this Database.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this Database.
        The national character set for the database.


        :param ncharacter_set: The ncharacter_set of this Database.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def db_home_id(self):
        """
        Gets the db_home_id of this Database.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_home_id of this Database.
        :rtype: str
        """
        return self._db_home_id

    @db_home_id.setter
    def db_home_id(self, db_home_id):
        """
        Sets the db_home_id of this Database.
        The `OCID`__ of the Database Home.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_home_id: The db_home_id of this Database.
        :type: str
        """
        self._db_home_id = db_home_id

    @property
    def db_system_id(self):
        """
        Gets the db_system_id of this Database.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The db_system_id of this Database.
        :rtype: str
        """
        return self._db_system_id

    @db_system_id.setter
    def db_system_id(self, db_system_id):
        """
        Sets the db_system_id of this Database.
        The `OCID`__ of the DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param db_system_id: The db_system_id of this Database.
        :type: str
        """
        self._db_system_id = db_system_id

    @property
    def vm_cluster_id(self):
        """
        Gets the vm_cluster_id of this Database.
        The `OCID`__ of the VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_id of this Database.
        :rtype: str
        """
        return self._vm_cluster_id

    @vm_cluster_id.setter
    def vm_cluster_id(self, vm_cluster_id):
        """
        Sets the vm_cluster_id of this Database.
        The `OCID`__ of the VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_id: The vm_cluster_id of this Database.
        :type: str
        """
        self._vm_cluster_id = vm_cluster_id

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this Database.
        The database name.


        :return: The db_name of this Database.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this Database.
        The database name.


        :param db_name: The db_name of this Database.
        :type: str
        """
        self._db_name = db_name

    @property
    def pdb_name(self):
        """
        Gets the pdb_name of this Database.
        The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.


        :return: The pdb_name of this Database.
        :rtype: str
        """
        return self._pdb_name

    @pdb_name.setter
    def pdb_name(self, pdb_name):
        """
        Sets the pdb_name of this Database.
        The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.


        :param pdb_name: The pdb_name of this Database.
        :type: str
        """
        self._pdb_name = pdb_name

    @property
    def db_workload(self):
        """
        Gets the db_workload of this Database.
        The database workload type.


        :return: The db_workload of this Database.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this Database.
        The database workload type.


        :param db_workload: The db_workload of this Database.
        :type: str
        """
        self._db_workload = db_workload

    @property
    def db_unique_name(self):
        """
        **[Required]** Gets the db_unique_name of this Database.
        A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby databases). The unique name cannot be changed.


        :return: The db_unique_name of this Database.
        :rtype: str
        """
        return self._db_unique_name

    @db_unique_name.setter
    def db_unique_name(self, db_unique_name):
        """
        Sets the db_unique_name of this Database.
        A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby databases). The unique name cannot be changed.


        :param db_unique_name: The db_unique_name of this Database.
        :type: str
        """
        self._db_unique_name = db_unique_name

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Database.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this Database.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Database.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this Database.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Database.
        The current state of the database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "UPGRADING", "CONVERTING", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Database.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Database.
        The current state of the database.


        :param lifecycle_state: The lifecycle_state of this Database.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "UPDATING", "BACKUP_IN_PROGRESS", "UPGRADING", "CONVERTING", "TERMINATING", "TERMINATED", "RESTORE_FAILED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        Gets the time_created of this Database.
        The date and time the database was created.


        :return: The time_created of this Database.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Database.
        The date and time the database was created.


        :param time_created: The time_created of this Database.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def last_backup_timestamp(self):
        """
        Gets the last_backup_timestamp of this Database.
        The date and time when the latest database backup was created.


        :return: The last_backup_timestamp of this Database.
        :rtype: datetime
        """
        return self._last_backup_timestamp

    @last_backup_timestamp.setter
    def last_backup_timestamp(self, last_backup_timestamp):
        """
        Sets the last_backup_timestamp of this Database.
        The date and time when the latest database backup was created.


        :param last_backup_timestamp: The last_backup_timestamp of this Database.
        :type: datetime
        """
        self._last_backup_timestamp = last_backup_timestamp

    @property
    def db_backup_config(self):
        """
        Gets the db_backup_config of this Database.

        :return: The db_backup_config of this Database.
        :rtype: oci.database.models.DbBackupConfig
        """
        return self._db_backup_config

    @db_backup_config.setter
    def db_backup_config(self, db_backup_config):
        """
        Sets the db_backup_config of this Database.

        :param db_backup_config: The db_backup_config of this Database.
        :type: oci.database.models.DbBackupConfig
        """
        self._db_backup_config = db_backup_config

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Database.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Database.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Database.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Database.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Database.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Database.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Database.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Database.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def connection_strings(self):
        """
        Gets the connection_strings of this Database.
        The Connection strings used to connect to the Oracle Database.


        :return: The connection_strings of this Database.
        :rtype: oci.database.models.DatabaseConnectionStrings
        """
        return self._connection_strings

    @connection_strings.setter
    def connection_strings(self, connection_strings):
        """
        Sets the connection_strings of this Database.
        The Connection strings used to connect to the Oracle Database.


        :param connection_strings: The connection_strings of this Database.
        :type: oci.database.models.DatabaseConnectionStrings
        """
        self._connection_strings = connection_strings

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this Database.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this Database.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this Database.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this Database.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def kms_key_version_id(self):
        """
        Gets the kms_key_version_id of this Database.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :return: The kms_key_version_id of this Database.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this Database.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :param kms_key_version_id: The kms_key_version_id of this Database.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this Database.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this Database.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this Database.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this Database.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def source_database_point_in_time_recovery_timestamp(self):
        """
        Gets the source_database_point_in_time_recovery_timestamp of this Database.
        Point in time recovery timeStamp of the source database at which cloned database system is cloned from the source database system, as described in `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The source_database_point_in_time_recovery_timestamp of this Database.
        :rtype: datetime
        """
        return self._source_database_point_in_time_recovery_timestamp

    @source_database_point_in_time_recovery_timestamp.setter
    def source_database_point_in_time_recovery_timestamp(self, source_database_point_in_time_recovery_timestamp):
        """
        Sets the source_database_point_in_time_recovery_timestamp of this Database.
        Point in time recovery timeStamp of the source database at which cloned database system is cloned from the source database system, as described in `RFC 3339`__

        __ https://tools.ietf.org/rfc/rfc3339


        :param source_database_point_in_time_recovery_timestamp: The source_database_point_in_time_recovery_timestamp of this Database.
        :type: datetime
        """
        self._source_database_point_in_time_recovery_timestamp = source_database_point_in_time_recovery_timestamp

    @property
    def database_software_image_id(self):
        """
        Gets the database_software_image_id of this Database.
        The database software image `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The database_software_image_id of this Database.
        :rtype: str
        """
        return self._database_software_image_id

    @database_software_image_id.setter
    def database_software_image_id(self, database_software_image_id):
        """
        Sets the database_software_image_id of this Database.
        The database software image `OCID`__

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param database_software_image_id: The database_software_image_id of this Database.
        :type: str
        """
        self._database_software_image_id = database_software_image_id

    @property
    def is_cdb(self):
        """
        Gets the is_cdb of this Database.
        True if the database is a container database.


        :return: The is_cdb of this Database.
        :rtype: bool
        """
        return self._is_cdb

    @is_cdb.setter
    def is_cdb(self, is_cdb):
        """
        Sets the is_cdb of this Database.
        True if the database is a container database.


        :param is_cdb: The is_cdb of this Database.
        :type: bool
        """
        self._is_cdb = is_cdb

    @property
    def database_management_config(self):
        """
        Gets the database_management_config of this Database.

        :return: The database_management_config of this Database.
        :rtype: oci.database.models.CloudDatabaseManagementConfig
        """
        return self._database_management_config

    @database_management_config.setter
    def database_management_config(self, database_management_config):
        """
        Sets the database_management_config of this Database.

        :param database_management_config: The database_management_config of this Database.
        :type: oci.database.models.CloudDatabaseManagementConfig
        """
        self._database_management_config = database_management_config

    @property
    def sid_prefix(self):
        """
        Gets the sid_prefix of this Database.
        Specifies a prefix for the `Oracle SID` of the database to be created.


        :return: The sid_prefix of this Database.
        :rtype: str
        """
        return self._sid_prefix

    @sid_prefix.setter
    def sid_prefix(self, sid_prefix):
        """
        Sets the sid_prefix of this Database.
        Specifies a prefix for the `Oracle SID` of the database to be created.


        :param sid_prefix: The sid_prefix of this Database.
        :type: str
        """
        self._sid_prefix = sid_prefix

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
