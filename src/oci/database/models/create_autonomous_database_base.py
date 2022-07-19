# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDatabaseBase(object):
    """
    Details to create an Oracle Autonomous Database.

    **Notes:**
    - To specify OCPU core count, you must use either `ocpuCount` or `cpuCoreCount`. You cannot use both parameters at the same time.
    - To specify a storage allocation, you must use  either `dataStorageSizeInGBs` or `dataStorageSizeInTBs`.
    - See the individual parameter discriptions for more information on the OCPU and storage value parameters.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the db_workload property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the db_workload property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "AJD"
    DB_WORKLOAD_AJD = "AJD"

    #: A constant which can be used with the db_workload property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "APEX"
    DB_WORKLOAD_APEX = "APEX"

    #: A constant which can be used with the license_model property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "NONE"
    SOURCE_NONE = "NONE"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "DATABASE"
    SOURCE_DATABASE = "DATABASE"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "BACKUP_FROM_ID"
    SOURCE_BACKUP_FROM_ID = "BACKUP_FROM_ID"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "BACKUP_FROM_TIMESTAMP"
    SOURCE_BACKUP_FROM_TIMESTAMP = "BACKUP_FROM_TIMESTAMP"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "CLONE_TO_REFRESHABLE"
    SOURCE_CLONE_TO_REFRESHABLE = "CLONE_TO_REFRESHABLE"

    #: A constant which can be used with the source property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "CROSS_REGION_DATAGUARD"
    SOURCE_CROSS_REGION_DATAGUARD = "CROSS_REGION_DATAGUARD"

    #: A constant which can be used with the autonomous_maintenance_schedule_type property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "EARLY"
    AUTONOMOUS_MAINTENANCE_SCHEDULE_TYPE_EARLY = "EARLY"

    #: A constant which can be used with the autonomous_maintenance_schedule_type property of a CreateAutonomousDatabaseBase.
    #: This constant has a value of "REGULAR"
    AUTONOMOUS_MAINTENANCE_SCHEDULE_TYPE_REGULAR = "REGULAR"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDatabaseBase object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.database.models.CreateAutonomousDatabaseCloneDetails`
        * :class:`~oci.database.models.CreateRefreshableAutonomousDatabaseCloneDetails`
        * :class:`~oci.database.models.CreateAutonomousDatabaseFromBackupDetails`
        * :class:`~oci.database.models.CreateAutonomousDatabaseFromBackupTimestampDetails`
        * :class:`~oci.database.models.CreateCrossRegionAutonomousDatabaseDataGuardDetails`
        * :class:`~oci.database.models.CreateAutonomousDatabaseDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousDatabaseBase.
        :type compartment_id: str

        :param character_set:
            The value to assign to the character_set property of this CreateAutonomousDatabaseBase.
        :type character_set: str

        :param ncharacter_set:
            The value to assign to the ncharacter_set property of this CreateAutonomousDatabaseBase.
        :type ncharacter_set: str

        :param db_name:
            The value to assign to the db_name property of this CreateAutonomousDatabaseBase.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateAutonomousDatabaseBase.
        :type cpu_core_count: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this CreateAutonomousDatabaseBase.
        :type ocpu_count: float

        :param db_workload:
            The value to assign to the db_workload property of this CreateAutonomousDatabaseBase.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateAutonomousDatabaseBase.
        :type data_storage_size_in_tbs: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this CreateAutonomousDatabaseBase.
        :type data_storage_size_in_gbs: int

        :param is_free_tier:
            The value to assign to the is_free_tier property of this CreateAutonomousDatabaseBase.
        :type is_free_tier: bool

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateAutonomousDatabaseBase.
        :type kms_key_id: str

        :param vault_id:
            The value to assign to the vault_id property of this CreateAutonomousDatabaseBase.
        :type vault_id: str

        :param admin_password:
            The value to assign to the admin_password property of this CreateAutonomousDatabaseBase.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDatabaseBase.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateAutonomousDatabaseBase.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_preview_version_with_service_terms_accepted:
            The value to assign to the is_preview_version_with_service_terms_accepted property of this CreateAutonomousDatabaseBase.
        :type is_preview_version_with_service_terms_accepted: bool

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateAutonomousDatabaseBase.
        :type is_auto_scaling_enabled: bool

        :param is_dedicated:
            The value to assign to the is_dedicated property of this CreateAutonomousDatabaseBase.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this CreateAutonomousDatabaseBase.
        :type autonomous_container_database_id: str

        :param is_access_control_enabled:
            The value to assign to the is_access_control_enabled property of this CreateAutonomousDatabaseBase.
        :type is_access_control_enabled: bool

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this CreateAutonomousDatabaseBase.
        :type whitelisted_ips: list[str]

        :param are_primary_whitelisted_ips_used:
            The value to assign to the are_primary_whitelisted_ips_used property of this CreateAutonomousDatabaseBase.
        :type are_primary_whitelisted_ips_used: bool

        :param standby_whitelisted_ips:
            The value to assign to the standby_whitelisted_ips property of this CreateAutonomousDatabaseBase.
        :type standby_whitelisted_ips: list[str]

        :param is_data_guard_enabled:
            The value to assign to the is_data_guard_enabled property of this CreateAutonomousDatabaseBase.
        :type is_data_guard_enabled: bool

        :param is_local_data_guard_enabled:
            The value to assign to the is_local_data_guard_enabled property of this CreateAutonomousDatabaseBase.
        :type is_local_data_guard_enabled: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateAutonomousDatabaseBase.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateAutonomousDatabaseBase.
        :type nsg_ids: list[str]

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this CreateAutonomousDatabaseBase.
        :type private_endpoint_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDatabaseBase.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDatabaseBase.
        :type defined_tags: dict(str, dict(str, object))

        :param db_version:
            The value to assign to the db_version property of this CreateAutonomousDatabaseBase.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateAutonomousDatabaseBase.
            Allowed values for this property are: "NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP", "CLONE_TO_REFRESHABLE", "CROSS_REGION_DATAGUARD"
        :type source: str

        :param customer_contacts:
            The value to assign to the customer_contacts property of this CreateAutonomousDatabaseBase.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        :param is_mtls_connection_required:
            The value to assign to the is_mtls_connection_required property of this CreateAutonomousDatabaseBase.
        :type is_mtls_connection_required: bool

        :param autonomous_maintenance_schedule_type:
            The value to assign to the autonomous_maintenance_schedule_type property of this CreateAutonomousDatabaseBase.
            Allowed values for this property are: "EARLY", "REGULAR"
        :type autonomous_maintenance_schedule_type: str

        :param scheduled_operations:
            The value to assign to the scheduled_operations property of this CreateAutonomousDatabaseBase.
        :type scheduled_operations: list[oci.database.models.ScheduledOperationDetails]

        :param is_auto_scaling_for_storage_enabled:
            The value to assign to the is_auto_scaling_for_storage_enabled property of this CreateAutonomousDatabaseBase.
        :type is_auto_scaling_for_storage_enabled: bool

        :param max_cpu_core_count:
            The value to assign to the max_cpu_core_count property of this CreateAutonomousDatabaseBase.
        :type max_cpu_core_count: int

        :param database_edition:
            The value to assign to the database_edition property of this CreateAutonomousDatabaseBase.
        :type database_edition: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'character_set': 'str',
            'ncharacter_set': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'ocpu_count': 'float',
            'db_workload': 'str',
            'data_storage_size_in_tbs': 'int',
            'data_storage_size_in_gbs': 'int',
            'is_free_tier': 'bool',
            'kms_key_id': 'str',
            'vault_id': 'str',
            'admin_password': 'str',
            'display_name': 'str',
            'license_model': 'str',
            'is_preview_version_with_service_terms_accepted': 'bool',
            'is_auto_scaling_enabled': 'bool',
            'is_dedicated': 'bool',
            'autonomous_container_database_id': 'str',
            'is_access_control_enabled': 'bool',
            'whitelisted_ips': 'list[str]',
            'are_primary_whitelisted_ips_used': 'bool',
            'standby_whitelisted_ips': 'list[str]',
            'is_data_guard_enabled': 'bool',
            'is_local_data_guard_enabled': 'bool',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'private_endpoint_label': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'db_version': 'str',
            'source': 'str',
            'customer_contacts': 'list[CustomerContact]',
            'is_mtls_connection_required': 'bool',
            'autonomous_maintenance_schedule_type': 'str',
            'scheduled_operations': 'list[ScheduledOperationDetails]',
            'is_auto_scaling_for_storage_enabled': 'bool',
            'max_cpu_core_count': 'int',
            'database_edition': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'character_set': 'characterSet',
            'ncharacter_set': 'ncharacterSet',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'ocpu_count': 'ocpuCount',
            'db_workload': 'dbWorkload',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'is_free_tier': 'isFreeTier',
            'kms_key_id': 'kmsKeyId',
            'vault_id': 'vaultId',
            'admin_password': 'adminPassword',
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'is_preview_version_with_service_terms_accepted': 'isPreviewVersionWithServiceTermsAccepted',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'is_dedicated': 'isDedicated',
            'autonomous_container_database_id': 'autonomousContainerDatabaseId',
            'is_access_control_enabled': 'isAccessControlEnabled',
            'whitelisted_ips': 'whitelistedIps',
            'are_primary_whitelisted_ips_used': 'arePrimaryWhitelistedIpsUsed',
            'standby_whitelisted_ips': 'standbyWhitelistedIps',
            'is_data_guard_enabled': 'isDataGuardEnabled',
            'is_local_data_guard_enabled': 'isLocalDataGuardEnabled',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'private_endpoint_label': 'privateEndpointLabel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'db_version': 'dbVersion',
            'source': 'source',
            'customer_contacts': 'customerContacts',
            'is_mtls_connection_required': 'isMtlsConnectionRequired',
            'autonomous_maintenance_schedule_type': 'autonomousMaintenanceScheduleType',
            'scheduled_operations': 'scheduledOperations',
            'is_auto_scaling_for_storage_enabled': 'isAutoScalingForStorageEnabled',
            'max_cpu_core_count': 'maxCpuCoreCount',
            'database_edition': 'databaseEdition'
        }

        self._compartment_id = None
        self._character_set = None
        self._ncharacter_set = None
        self._db_name = None
        self._cpu_core_count = None
        self._ocpu_count = None
        self._db_workload = None
        self._data_storage_size_in_tbs = None
        self._data_storage_size_in_gbs = None
        self._is_free_tier = None
        self._kms_key_id = None
        self._vault_id = None
        self._admin_password = None
        self._display_name = None
        self._license_model = None
        self._is_preview_version_with_service_terms_accepted = None
        self._is_auto_scaling_enabled = None
        self._is_dedicated = None
        self._autonomous_container_database_id = None
        self._is_access_control_enabled = None
        self._whitelisted_ips = None
        self._are_primary_whitelisted_ips_used = None
        self._standby_whitelisted_ips = None
        self._is_data_guard_enabled = None
        self._is_local_data_guard_enabled = None
        self._subnet_id = None
        self._nsg_ids = None
        self._private_endpoint_label = None
        self._freeform_tags = None
        self._defined_tags = None
        self._db_version = None
        self._source = None
        self._customer_contacts = None
        self._is_mtls_connection_required = None
        self._autonomous_maintenance_schedule_type = None
        self._scheduled_operations = None
        self._is_auto_scaling_for_storage_enabled = None
        self._max_cpu_core_count = None
        self._database_edition = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['source']

        if type == 'DATABASE':
            return 'CreateAutonomousDatabaseCloneDetails'

        if type == 'CLONE_TO_REFRESHABLE':
            return 'CreateRefreshableAutonomousDatabaseCloneDetails'

        if type == 'BACKUP_FROM_ID':
            return 'CreateAutonomousDatabaseFromBackupDetails'

        if type == 'BACKUP_FROM_TIMESTAMP':
            return 'CreateAutonomousDatabaseFromBackupTimestampDetails'

        if type == 'CROSS_REGION_DATAGUARD':
            return 'CreateCrossRegionAutonomousDatabaseDataGuardDetails'

        if type == 'NONE':
            return 'CreateAutonomousDatabaseDetails'
        else:
            return 'CreateAutonomousDatabaseBase'

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the compartment of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the compartment of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def character_set(self):
        """
        Gets the character_set of this CreateAutonomousDatabaseBase.
        The character set for the autonomous database.  The default is AL32UTF8. Allowed values for an Autonomous Database on shared infrastructure as as returned by `List Autonomous Database Character Sets`__

        For an Autonomous Database on dedicated infrastructure, the allowed values are:

        AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS

        __ https://docs.cloud.oracle.com/autonomousDatabaseCharacterSets


        :return: The character_set of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._character_set

    @character_set.setter
    def character_set(self, character_set):
        """
        Sets the character_set of this CreateAutonomousDatabaseBase.
        The character set for the autonomous database.  The default is AL32UTF8. Allowed values for an Autonomous Database on shared infrastructure as as returned by `List Autonomous Database Character Sets`__

        For an Autonomous Database on dedicated infrastructure, the allowed values are:

        AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS

        __ https://docs.cloud.oracle.com/autonomousDatabaseCharacterSets


        :param character_set: The character_set of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._character_set = character_set

    @property
    def ncharacter_set(self):
        """
        Gets the ncharacter_set of this CreateAutonomousDatabaseBase.
        The character set for the Autonomous Database.  The default is AL32UTF8. Use :func:`list_autonomous_database_character_sets` to list the allowed values for an Autonomous Database on shared Exadata infrastructure.
        For an Autonomous Database on dedicated Exadata infrastructure, the allowed values are:
        AL16UTF16 or UTF8.


        :return: The ncharacter_set of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._ncharacter_set

    @ncharacter_set.setter
    def ncharacter_set(self, ncharacter_set):
        """
        Sets the ncharacter_set of this CreateAutonomousDatabaseBase.
        The character set for the Autonomous Database.  The default is AL32UTF8. Use :func:`list_autonomous_database_character_sets` to list the allowed values for an Autonomous Database on shared Exadata infrastructure.
        For an Autonomous Database on dedicated Exadata infrastructure, the allowed values are:
        AL16UTF16 or UTF8.


        :param ncharacter_set: The ncharacter_set of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._ncharacter_set = ncharacter_set

    @property
    def db_name(self):
        """
        Gets the db_name of this CreateAutonomousDatabaseBase.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :return: The db_name of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this CreateAutonomousDatabaseBase.
        The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :param db_name: The db_name of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._db_name = db_name

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this CreateAutonomousDatabaseBase.
        The number of OCPU cores to be made available to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `ocpuCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The cpu_core_count of this CreateAutonomousDatabaseBase.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this CreateAutonomousDatabaseBase.
        The number of OCPU cores to be made available to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `ocpuCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param cpu_core_count: The cpu_core_count of this CreateAutonomousDatabaseBase.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def ocpu_count(self):
        """
        Gets the ocpu_count of this CreateAutonomousDatabaseBase.
        The number of OCPU cores to be made available to the database.

        The following points apply:
        - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Databasese on shared Exadata infrastructure.)
        - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata infrastructure.

        For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The ocpu_count of this CreateAutonomousDatabaseBase.
        :rtype: float
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this CreateAutonomousDatabaseBase.
        The number of OCPU cores to be made available to the database.

        The following points apply:
        - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Databasese on shared Exadata infrastructure.)
        - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata infrastructure.

        For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param ocpu_count: The ocpu_count of this CreateAutonomousDatabaseBase.
        :type: float
        """
        self._ocpu_count = ocpu_count

    @property
    def db_workload(self):
        """
        Gets the db_workload of this CreateAutonomousDatabaseBase.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.

        Allowed values for this property are: "OLTP", "DW", "AJD", "APEX"


        :return: The db_workload of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this CreateAutonomousDatabaseBase.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.


        :param db_workload: The db_workload of this CreateAutonomousDatabaseBase.
        :type: str
        """
        allowed_values = ["OLTP", "DW", "AJD", "APEX"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            raise ValueError(
                "Invalid value for `db_workload`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._db_workload = db_workload

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. For Autonomous Databases on dedicated Exadata infrastructure, the maximum storage value is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `dataStorageSizeInGBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. For Autonomous Databases on dedicated Exadata infrastructure, the maximum storage value is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `dataStorageSizeInGBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this CreateAutonomousDatabaseBase.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this CreateAutonomousDatabaseBase.
        The size, in gigabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. The maximum storage value is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Notes**
        - This parameter is only supported for dedicated Exadata infrastructure.
        - This parameter cannot be used with the `dataStorageSizeInTBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The data_storage_size_in_gbs of this CreateAutonomousDatabaseBase.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this CreateAutonomousDatabaseBase.
        The size, in gigabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. The maximum storage value is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Notes**
        - This parameter is only supported for dedicated Exadata infrastructure.
        - This parameter cannot be used with the `dataStorageSizeInTBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this CreateAutonomousDatabaseBase.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def is_free_tier(self):
        """
        Gets the is_free_tier of this CreateAutonomousDatabaseBase.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :return: The is_free_tier of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_free_tier

    @is_free_tier.setter
    def is_free_tier(self, is_free_tier):
        """
        Sets the is_free_tier of this CreateAutonomousDatabaseBase.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :param is_free_tier: The is_free_tier of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_free_tier = is_free_tier

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this CreateAutonomousDatabaseBase.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this CreateAutonomousDatabaseBase.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def admin_password(self):
        """
        Gets the admin_password of this CreateAutonomousDatabaseBase.
        **Important** The `adminPassword` must be specified for all Autonomous Databases except for refreshable clones. The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :return: The admin_password of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this CreateAutonomousDatabaseBase.
        **Important** The `adminPassword` must be specified for all Autonomous Databases except for refreshable clones. The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing.


        :param admin_password: The admin_password of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAutonomousDatabaseBase.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :return: The display_name of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAutonomousDatabaseBase.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :param display_name: The display_name of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._display_name = display_name

    @property
    def license_model(self):
        """
        Gets the license_model of this CreateAutonomousDatabaseBase.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this CreateAutonomousDatabaseBase.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param license_model: The license_model of this CreateAutonomousDatabaseBase.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            raise ValueError(
                "Invalid value for `license_model`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._license_model = license_model

    @property
    def is_preview_version_with_service_terms_accepted(self):
        """
        Gets the is_preview_version_with_service_terms_accepted of this CreateAutonomousDatabaseBase.
        If set to `TRUE`, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for databases on `shared Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The is_preview_version_with_service_terms_accepted of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_preview_version_with_service_terms_accepted

    @is_preview_version_with_service_terms_accepted.setter
    def is_preview_version_with_service_terms_accepted(self, is_preview_version_with_service_terms_accepted):
        """
        Sets the is_preview_version_with_service_terms_accepted of this CreateAutonomousDatabaseBase.
        If set to `TRUE`, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have been accepted. Note that preview version software is only available for databases on `shared Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param is_preview_version_with_service_terms_accepted: The is_preview_version_with_service_terms_accepted of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_preview_version_with_service_terms_accepted = is_preview_version_with_service_terms_accepted

    @property
    def is_auto_scaling_enabled(self):
        """
        Gets the is_auto_scaling_enabled of this CreateAutonomousDatabaseBase.
        Indicates if auto scaling is enabled for the Autonomous Database OCPU core count. The default value is `FALSE`.


        :return: The is_auto_scaling_enabled of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this CreateAutonomousDatabaseBase.
        Indicates if auto scaling is enabled for the Autonomous Database OCPU core count. The default value is `FALSE`.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def is_dedicated(self):
        """
        Gets the is_dedicated of this CreateAutonomousDatabaseBase.
        True if the database is on `dedicated Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The is_dedicated of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_dedicated

    @is_dedicated.setter
    def is_dedicated(self, is_dedicated):
        """
        Sets the is_dedicated of this CreateAutonomousDatabaseBase.
        True if the database is on `dedicated Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param is_dedicated: The is_dedicated of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_dedicated = is_dedicated

    @property
    def autonomous_container_database_id(self):
        """
        Gets the autonomous_container_database_id of this CreateAutonomousDatabaseBase.
        The Autonomous Container Database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_container_database_id of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._autonomous_container_database_id

    @autonomous_container_database_id.setter
    def autonomous_container_database_id(self, autonomous_container_database_id):
        """
        Sets the autonomous_container_database_id of this CreateAutonomousDatabaseBase.
        The Autonomous Container Database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_container_database_id: The autonomous_container_database_id of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._autonomous_container_database_id = autonomous_container_database_id

    @property
    def is_access_control_enabled(self):
        """
        Gets the is_access_control_enabled of this CreateAutonomousDatabaseBase.
        Indicates if the database-level access control is enabled.
        If disabled, database access is defined by the network security rules.
        If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,
         if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console.
        When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

        This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.


        :return: The is_access_control_enabled of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_access_control_enabled

    @is_access_control_enabled.setter
    def is_access_control_enabled(self, is_access_control_enabled):
        """
        Sets the is_access_control_enabled of this CreateAutonomousDatabaseBase.
        Indicates if the database-level access control is enabled.
        If disabled, database access is defined by the network security rules.
        If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,
         if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console.
        When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

        This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.


        :param is_access_control_enabled: The is_access_control_enabled of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_access_control_enabled = is_access_control_enabled

    @property
    def whitelisted_ips(self):
        """
        Gets the whitelisted_ips of this CreateAutonomousDatabaseBase.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The whitelisted_ips of this CreateAutonomousDatabaseBase.
        :rtype: list[str]
        """
        return self._whitelisted_ips

    @whitelisted_ips.setter
    def whitelisted_ips(self, whitelisted_ips):
        """
        Sets the whitelisted_ips of this CreateAutonomousDatabaseBase.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param whitelisted_ips: The whitelisted_ips of this CreateAutonomousDatabaseBase.
        :type: list[str]
        """
        self._whitelisted_ips = whitelisted_ips

    @property
    def are_primary_whitelisted_ips_used(self):
        """
        Gets the are_primary_whitelisted_ips_used of this CreateAutonomousDatabaseBase.
        This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
        It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby.
        It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.


        :return: The are_primary_whitelisted_ips_used of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._are_primary_whitelisted_ips_used

    @are_primary_whitelisted_ips_used.setter
    def are_primary_whitelisted_ips_used(self, are_primary_whitelisted_ips_used):
        """
        Sets the are_primary_whitelisted_ips_used of this CreateAutonomousDatabaseBase.
        This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
        It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby.
        It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.


        :param are_primary_whitelisted_ips_used: The are_primary_whitelisted_ips_used of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._are_primary_whitelisted_ips_used = are_primary_whitelisted_ips_used

    @property
    def standby_whitelisted_ips(self):
        """
        Gets the standby_whitelisted_ips of this CreateAutonomousDatabaseBase.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The standby_whitelisted_ips of this CreateAutonomousDatabaseBase.
        :rtype: list[str]
        """
        return self._standby_whitelisted_ips

    @standby_whitelisted_ips.setter
    def standby_whitelisted_ips(self, standby_whitelisted_ips):
        """
        Sets the standby_whitelisted_ips of this CreateAutonomousDatabaseBase.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param standby_whitelisted_ips: The standby_whitelisted_ips of this CreateAutonomousDatabaseBase.
        :type: list[str]
        """
        self._standby_whitelisted_ips = standby_whitelisted_ips

    @property
    def is_data_guard_enabled(self):
        """
        Gets the is_data_guard_enabled of this CreateAutonomousDatabaseBase.
        **Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.


        :return: The is_data_guard_enabled of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_data_guard_enabled

    @is_data_guard_enabled.setter
    def is_data_guard_enabled(self, is_data_guard_enabled):
        """
        Sets the is_data_guard_enabled of this CreateAutonomousDatabaseBase.
        **Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.


        :param is_data_guard_enabled: The is_data_guard_enabled of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_data_guard_enabled = is_data_guard_enabled

    @property
    def is_local_data_guard_enabled(self):
        """
        Gets the is_local_data_guard_enabled of this CreateAutonomousDatabaseBase.
        Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.


        :return: The is_local_data_guard_enabled of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_local_data_guard_enabled

    @is_local_data_guard_enabled.setter
    def is_local_data_guard_enabled(self, is_local_data_guard_enabled):
        """
        Sets the is_local_data_guard_enabled of this CreateAutonomousDatabaseBase.
        Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.


        :param is_local_data_guard_enabled: The is_local_data_guard_enabled of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_local_data_guard_enabled = is_local_data_guard_enabled

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateAutonomousDatabaseBase.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateAutonomousDatabaseBase.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this CreateAutonomousDatabaseBase.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateAutonomousDatabaseBase.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this CreateAutonomousDatabaseBase.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def private_endpoint_label(self):
        """
        Gets the private_endpoint_label of this CreateAutonomousDatabaseBase.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :return: The private_endpoint_label of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._private_endpoint_label

    @private_endpoint_label.setter
    def private_endpoint_label(self, private_endpoint_label):
        """
        Sets the private_endpoint_label of this CreateAutonomousDatabaseBase.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :param private_endpoint_label: The private_endpoint_label of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._private_endpoint_label = private_endpoint_label

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAutonomousDatabaseBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateAutonomousDatabaseBase.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAutonomousDatabaseBase.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateAutonomousDatabaseBase.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAutonomousDatabaseBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateAutonomousDatabaseBase.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAutonomousDatabaseBase.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateAutonomousDatabaseBase.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def db_version(self):
        """
        Gets the db_version of this CreateAutonomousDatabaseBase.
        A valid Oracle Database version for Autonomous Database.


        :return: The db_version of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this CreateAutonomousDatabaseBase.
        A valid Oracle Database version for Autonomous Database.


        :param db_version: The db_version of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._db_version = db_version

    @property
    def source(self):
        """
        Gets the source of this CreateAutonomousDatabaseBase.
        The source of the database: Use `NONE` for creating a new Autonomous Database. Use `DATABASE` for creating a new Autonomous Database by cloning an existing Autonomous Database. Use `CROSS_REGION_DATAGUARD` to create a standby Data Guard database in another region.

        For Autonomous Databases on `shared Exadata infrastructure`__, the following cloning options are available: Use `BACKUP_FROM_ID` for creating a new Autonomous Database from a specified backup. Use `BACKUP_FROM_TIMESTAMP` for creating a point-in-time Autonomous Database clone using backups. For more information, see `Cloning and Moving an Autonomous Database`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/clone-autonomous-database.html#GUID-D771796F-5081-4CFB-A7FF-0F893EABD7BC

        Allowed values for this property are: "NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP", "CLONE_TO_REFRESHABLE", "CROSS_REGION_DATAGUARD"


        :return: The source of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """
        Sets the source of this CreateAutonomousDatabaseBase.
        The source of the database: Use `NONE` for creating a new Autonomous Database. Use `DATABASE` for creating a new Autonomous Database by cloning an existing Autonomous Database. Use `CROSS_REGION_DATAGUARD` to create a standby Data Guard database in another region.

        For Autonomous Databases on `shared Exadata infrastructure`__, the following cloning options are available: Use `BACKUP_FROM_ID` for creating a new Autonomous Database from a specified backup. Use `BACKUP_FROM_TIMESTAMP` for creating a point-in-time Autonomous Database clone using backups. For more information, see `Cloning and Moving an Autonomous Database`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/clone-autonomous-database.html#GUID-D771796F-5081-4CFB-A7FF-0F893EABD7BC


        :param source: The source of this CreateAutonomousDatabaseBase.
        :type: str
        """
        allowed_values = ["NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP", "CLONE_TO_REFRESHABLE", "CROSS_REGION_DATAGUARD"]
        if not value_allowed_none_or_none_sentinel(source, allowed_values):
            raise ValueError(
                "Invalid value for `source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._source = source

    @property
    def customer_contacts(self):
        """
        Gets the customer_contacts of this CreateAutonomousDatabaseBase.
        Customer Contacts.


        :return: The customer_contacts of this CreateAutonomousDatabaseBase.
        :rtype: list[oci.database.models.CustomerContact]
        """
        return self._customer_contacts

    @customer_contacts.setter
    def customer_contacts(self, customer_contacts):
        """
        Sets the customer_contacts of this CreateAutonomousDatabaseBase.
        Customer Contacts.


        :param customer_contacts: The customer_contacts of this CreateAutonomousDatabaseBase.
        :type: list[oci.database.models.CustomerContact]
        """
        self._customer_contacts = customer_contacts

    @property
    def is_mtls_connection_required(self):
        """
        Gets the is_mtls_connection_required of this CreateAutonomousDatabaseBase.
        Indicates whether the Autonomous Database requires mTLS connections.


        :return: The is_mtls_connection_required of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_mtls_connection_required

    @is_mtls_connection_required.setter
    def is_mtls_connection_required(self, is_mtls_connection_required):
        """
        Sets the is_mtls_connection_required of this CreateAutonomousDatabaseBase.
        Indicates whether the Autonomous Database requires mTLS connections.


        :param is_mtls_connection_required: The is_mtls_connection_required of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_mtls_connection_required = is_mtls_connection_required

    @property
    def autonomous_maintenance_schedule_type(self):
        """
        Gets the autonomous_maintenance_schedule_type of this CreateAutonomousDatabaseBase.
        The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database
        follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.

        Allowed values for this property are: "EARLY", "REGULAR"


        :return: The autonomous_maintenance_schedule_type of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._autonomous_maintenance_schedule_type

    @autonomous_maintenance_schedule_type.setter
    def autonomous_maintenance_schedule_type(self, autonomous_maintenance_schedule_type):
        """
        Sets the autonomous_maintenance_schedule_type of this CreateAutonomousDatabaseBase.
        The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database
        follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.


        :param autonomous_maintenance_schedule_type: The autonomous_maintenance_schedule_type of this CreateAutonomousDatabaseBase.
        :type: str
        """
        allowed_values = ["EARLY", "REGULAR"]
        if not value_allowed_none_or_none_sentinel(autonomous_maintenance_schedule_type, allowed_values):
            raise ValueError(
                "Invalid value for `autonomous_maintenance_schedule_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._autonomous_maintenance_schedule_type = autonomous_maintenance_schedule_type

    @property
    def scheduled_operations(self):
        """
        Gets the scheduled_operations of this CreateAutonomousDatabaseBase.
        list of scheduled operations


        :return: The scheduled_operations of this CreateAutonomousDatabaseBase.
        :rtype: list[oci.database.models.ScheduledOperationDetails]
        """
        return self._scheduled_operations

    @scheduled_operations.setter
    def scheduled_operations(self, scheduled_operations):
        """
        Sets the scheduled_operations of this CreateAutonomousDatabaseBase.
        list of scheduled operations


        :param scheduled_operations: The scheduled_operations of this CreateAutonomousDatabaseBase.
        :type: list[oci.database.models.ScheduledOperationDetails]
        """
        self._scheduled_operations = scheduled_operations

    @property
    def is_auto_scaling_for_storage_enabled(self):
        """
        Gets the is_auto_scaling_for_storage_enabled of this CreateAutonomousDatabaseBase.
        Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.


        :return: The is_auto_scaling_for_storage_enabled of this CreateAutonomousDatabaseBase.
        :rtype: bool
        """
        return self._is_auto_scaling_for_storage_enabled

    @is_auto_scaling_for_storage_enabled.setter
    def is_auto_scaling_for_storage_enabled(self, is_auto_scaling_for_storage_enabled):
        """
        Sets the is_auto_scaling_for_storage_enabled of this CreateAutonomousDatabaseBase.
        Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.


        :param is_auto_scaling_for_storage_enabled: The is_auto_scaling_for_storage_enabled of this CreateAutonomousDatabaseBase.
        :type: bool
        """
        self._is_auto_scaling_for_storage_enabled = is_auto_scaling_for_storage_enabled

    @property
    def max_cpu_core_count(self):
        """
        Gets the max_cpu_core_count of this CreateAutonomousDatabaseBase.
        The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.


        :return: The max_cpu_core_count of this CreateAutonomousDatabaseBase.
        :rtype: int
        """
        return self._max_cpu_core_count

    @max_cpu_core_count.setter
    def max_cpu_core_count(self, max_cpu_core_count):
        """
        Sets the max_cpu_core_count of this CreateAutonomousDatabaseBase.
        The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.


        :param max_cpu_core_count: The max_cpu_core_count of this CreateAutonomousDatabaseBase.
        :type: int
        """
        self._max_cpu_core_count = max_cpu_core_count

    @property
    def database_edition(self):
        """
        Gets the database_edition of this CreateAutonomousDatabaseBase.
        The Oracle Database Edition that applies to the Autonomous databases.


        :return: The database_edition of this CreateAutonomousDatabaseBase.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this CreateAutonomousDatabaseBase.
        The Oracle Database Edition that applies to the Autonomous databases.


        :param database_edition: The database_edition of this CreateAutonomousDatabaseBase.
        :type: str
        """
        self._database_edition = database_edition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
