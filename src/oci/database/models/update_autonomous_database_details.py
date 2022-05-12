# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateAutonomousDatabaseDetails(object):
    """
    Details to update an Oracle Autonomous Database.

    **Notes**
    - To specify OCPU core count, you must use either `ocpuCount` or `cpuCoreCount`. You cannot use both parameters at the same time.
    - To specify a storage allocation, you must use  either `dataStorageSizeInGBs` or `dataStorageSizeInTBs`.
    - See the individual parameter discriptions for more information on the OCPU and storage value parameters.
    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the db_workload property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the db_workload property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "AJD"
    DB_WORKLOAD_AJD = "AJD"

    #: A constant which can be used with the db_workload property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "APEX"
    DB_WORKLOAD_APEX = "APEX"

    #: A constant which can be used with the license_model property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the refreshable_mode property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "AUTOMATIC"
    REFRESHABLE_MODE_AUTOMATIC = "AUTOMATIC"

    #: A constant which can be used with the refreshable_mode property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "MANUAL"
    REFRESHABLE_MODE_MANUAL = "MANUAL"

    #: A constant which can be used with the open_mode property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "READ_ONLY"
    OPEN_MODE_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the open_mode property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "READ_WRITE"
    OPEN_MODE_READ_WRITE = "READ_WRITE"

    #: A constant which can be used with the permission_level property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "RESTRICTED"
    PERMISSION_LEVEL_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the permission_level property of a UpdateAutonomousDatabaseDetails.
    #: This constant has a value of "UNRESTRICTED"
    PERMISSION_LEVEL_UNRESTRICTED = "UNRESTRICTED"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateAutonomousDatabaseDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this UpdateAutonomousDatabaseDetails.
        :type cpu_core_count: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this UpdateAutonomousDatabaseDetails.
        :type ocpu_count: float

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this UpdateAutonomousDatabaseDetails.
        :type data_storage_size_in_tbs: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this UpdateAutonomousDatabaseDetails.
        :type data_storage_size_in_gbs: int

        :param display_name:
            The value to assign to the display_name property of this UpdateAutonomousDatabaseDetails.
        :type display_name: str

        :param is_free_tier:
            The value to assign to the is_free_tier property of this UpdateAutonomousDatabaseDetails.
        :type is_free_tier: bool

        :param admin_password:
            The value to assign to the admin_password property of this UpdateAutonomousDatabaseDetails.
        :type admin_password: str

        :param db_name:
            The value to assign to the db_name property of this UpdateAutonomousDatabaseDetails.
        :type db_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateAutonomousDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateAutonomousDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param db_workload:
            The value to assign to the db_workload property of this UpdateAutonomousDatabaseDetails.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX"
        :type db_workload: str

        :param license_model:
            The value to assign to the license_model property of this UpdateAutonomousDatabaseDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_access_control_enabled:
            The value to assign to the is_access_control_enabled property of this UpdateAutonomousDatabaseDetails.
        :type is_access_control_enabled: bool

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this UpdateAutonomousDatabaseDetails.
        :type whitelisted_ips: list[str]

        :param are_primary_whitelisted_ips_used:
            The value to assign to the are_primary_whitelisted_ips_used property of this UpdateAutonomousDatabaseDetails.
        :type are_primary_whitelisted_ips_used: bool

        :param standby_whitelisted_ips:
            The value to assign to the standby_whitelisted_ips property of this UpdateAutonomousDatabaseDetails.
        :type standby_whitelisted_ips: list[str]

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this UpdateAutonomousDatabaseDetails.
        :type is_auto_scaling_enabled: bool

        :param is_refreshable_clone:
            The value to assign to the is_refreshable_clone property of this UpdateAutonomousDatabaseDetails.
        :type is_refreshable_clone: bool

        :param refreshable_mode:
            The value to assign to the refreshable_mode property of this UpdateAutonomousDatabaseDetails.
            Allowed values for this property are: "AUTOMATIC", "MANUAL"
        :type refreshable_mode: str

        :param is_local_data_guard_enabled:
            The value to assign to the is_local_data_guard_enabled property of this UpdateAutonomousDatabaseDetails.
        :type is_local_data_guard_enabled: bool

        :param is_data_guard_enabled:
            The value to assign to the is_data_guard_enabled property of this UpdateAutonomousDatabaseDetails.
        :type is_data_guard_enabled: bool

        :param peer_db_id:
            The value to assign to the peer_db_id property of this UpdateAutonomousDatabaseDetails.
        :type peer_db_id: str

        :param db_version:
            The value to assign to the db_version property of this UpdateAutonomousDatabaseDetails.
        :type db_version: str

        :param open_mode:
            The value to assign to the open_mode property of this UpdateAutonomousDatabaseDetails.
            Allowed values for this property are: "READ_ONLY", "READ_WRITE"
        :type open_mode: str

        :param permission_level:
            The value to assign to the permission_level property of this UpdateAutonomousDatabaseDetails.
            Allowed values for this property are: "RESTRICTED", "UNRESTRICTED"
        :type permission_level: str

        :param subnet_id:
            The value to assign to the subnet_id property of this UpdateAutonomousDatabaseDetails.
        :type subnet_id: str

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this UpdateAutonomousDatabaseDetails.
        :type private_endpoint_label: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this UpdateAutonomousDatabaseDetails.
        :type nsg_ids: list[str]

        :param customer_contacts:
            The value to assign to the customer_contacts property of this UpdateAutonomousDatabaseDetails.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        :param is_mtls_connection_required:
            The value to assign to the is_mtls_connection_required property of this UpdateAutonomousDatabaseDetails.
        :type is_mtls_connection_required: bool

        :param scheduled_operations:
            The value to assign to the scheduled_operations property of this UpdateAutonomousDatabaseDetails.
        :type scheduled_operations: list[oci.database.models.ScheduledOperationDetails]

        :param is_auto_scaling_for_storage_enabled:
            The value to assign to the is_auto_scaling_for_storage_enabled property of this UpdateAutonomousDatabaseDetails.
        :type is_auto_scaling_for_storage_enabled: bool

        :param max_cpu_core_count:
            The value to assign to the max_cpu_core_count property of this UpdateAutonomousDatabaseDetails.
        :type max_cpu_core_count: int

        :param database_edition:
            The value to assign to the database_edition property of this UpdateAutonomousDatabaseDetails.
        :type database_edition: str

        """
        self.swagger_types = {
            'cpu_core_count': 'int',
            'ocpu_count': 'float',
            'data_storage_size_in_tbs': 'int',
            'data_storage_size_in_gbs': 'int',
            'display_name': 'str',
            'is_free_tier': 'bool',
            'admin_password': 'str',
            'db_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'db_workload': 'str',
            'license_model': 'str',
            'is_access_control_enabled': 'bool',
            'whitelisted_ips': 'list[str]',
            'are_primary_whitelisted_ips_used': 'bool',
            'standby_whitelisted_ips': 'list[str]',
            'is_auto_scaling_enabled': 'bool',
            'is_refreshable_clone': 'bool',
            'refreshable_mode': 'str',
            'is_local_data_guard_enabled': 'bool',
            'is_data_guard_enabled': 'bool',
            'peer_db_id': 'str',
            'db_version': 'str',
            'open_mode': 'str',
            'permission_level': 'str',
            'subnet_id': 'str',
            'private_endpoint_label': 'str',
            'nsg_ids': 'list[str]',
            'customer_contacts': 'list[CustomerContact]',
            'is_mtls_connection_required': 'bool',
            'scheduled_operations': 'list[ScheduledOperationDetails]',
            'is_auto_scaling_for_storage_enabled': 'bool',
            'max_cpu_core_count': 'int',
            'database_edition': 'str'
        }

        self.attribute_map = {
            'cpu_core_count': 'cpuCoreCount',
            'ocpu_count': 'ocpuCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'display_name': 'displayName',
            'is_free_tier': 'isFreeTier',
            'admin_password': 'adminPassword',
            'db_name': 'dbName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'db_workload': 'dbWorkload',
            'license_model': 'licenseModel',
            'is_access_control_enabled': 'isAccessControlEnabled',
            'whitelisted_ips': 'whitelistedIps',
            'are_primary_whitelisted_ips_used': 'arePrimaryWhitelistedIpsUsed',
            'standby_whitelisted_ips': 'standbyWhitelistedIps',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'is_refreshable_clone': 'isRefreshableClone',
            'refreshable_mode': 'refreshableMode',
            'is_local_data_guard_enabled': 'isLocalDataGuardEnabled',
            'is_data_guard_enabled': 'isDataGuardEnabled',
            'peer_db_id': 'peerDbId',
            'db_version': 'dbVersion',
            'open_mode': 'openMode',
            'permission_level': 'permissionLevel',
            'subnet_id': 'subnetId',
            'private_endpoint_label': 'privateEndpointLabel',
            'nsg_ids': 'nsgIds',
            'customer_contacts': 'customerContacts',
            'is_mtls_connection_required': 'isMtlsConnectionRequired',
            'scheduled_operations': 'scheduledOperations',
            'is_auto_scaling_for_storage_enabled': 'isAutoScalingForStorageEnabled',
            'max_cpu_core_count': 'maxCpuCoreCount',
            'database_edition': 'databaseEdition'
        }

        self._cpu_core_count = None
        self._ocpu_count = None
        self._data_storage_size_in_tbs = None
        self._data_storage_size_in_gbs = None
        self._display_name = None
        self._is_free_tier = None
        self._admin_password = None
        self._db_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._db_workload = None
        self._license_model = None
        self._is_access_control_enabled = None
        self._whitelisted_ips = None
        self._are_primary_whitelisted_ips_used = None
        self._standby_whitelisted_ips = None
        self._is_auto_scaling_enabled = None
        self._is_refreshable_clone = None
        self._refreshable_mode = None
        self._is_local_data_guard_enabled = None
        self._is_data_guard_enabled = None
        self._peer_db_id = None
        self._db_version = None
        self._open_mode = None
        self._permission_level = None
        self._subnet_id = None
        self._private_endpoint_label = None
        self._nsg_ids = None
        self._customer_contacts = None
        self._is_mtls_connection_required = None
        self._scheduled_operations = None
        self._is_auto_scaling_for_storage_enabled = None
        self._max_cpu_core_count = None
        self._database_edition = None

    @property
    def cpu_core_count(self):
        """
        Gets the cpu_core_count of this UpdateAutonomousDatabaseDetails.
        The number of OCPU cores to be made available to the Autonomous Database.

        **Note:** This parameter cannot be used with the `ocpuCount` parameter.


        :return: The cpu_core_count of this UpdateAutonomousDatabaseDetails.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this UpdateAutonomousDatabaseDetails.
        The number of OCPU cores to be made available to the Autonomous Database.

        **Note:** This parameter cannot be used with the `ocpuCount` parameter.


        :param cpu_core_count: The cpu_core_count of this UpdateAutonomousDatabaseDetails.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def ocpu_count(self):
        """
        Gets the ocpu_count of this UpdateAutonomousDatabaseDetails.
        The number of OCPU cores to be made available to the Autonomous Database.

        For databases on dedicated Exadata infrastructure, you can specify a fractional value for this parameter. Fractional values are not supported for Autonomous Database on shared Exadata infrastructure.

        To provision less than 1 core, enter a fractional value in an increment of 0.1. To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available to the infrastructure shape. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. Likewise, you can provision 2 cores or 3 cores, but not 2.5 cores. The maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The ocpu_count of this UpdateAutonomousDatabaseDetails.
        :rtype: float
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this UpdateAutonomousDatabaseDetails.
        The number of OCPU cores to be made available to the Autonomous Database.

        For databases on dedicated Exadata infrastructure, you can specify a fractional value for this parameter. Fractional values are not supported for Autonomous Database on shared Exadata infrastructure.

        To provision less than 1 core, enter a fractional value in an increment of 0.1. To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available to the infrastructure shape. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. Likewise, you can provision 2 cores or 3 cores, but not 2.5 cores. The maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param ocpu_count: The ocpu_count of this UpdateAutonomousDatabaseDetails.
        :type: float
        """
        self._ocpu_count = ocpu_count

    @property
    def data_storage_size_in_tbs(self):
        """
        Gets the data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        The size, in terabytes, of the data volume that will be created and attached to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum storage value is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `dataStorageSizeInGBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        The size, in terabytes, of the data volume that will be created and attached to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum storage value is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `dataStorageSizeInGBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this UpdateAutonomousDatabaseDetails.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this UpdateAutonomousDatabaseDetails.
        Applies to dedicated Exadata infrastructure only.

        The size, in gigabytes, of the data volume that will be created and attached to the database. The maximum storage value depends on the system shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `dataStorageSizeInTBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The data_storage_size_in_gbs of this UpdateAutonomousDatabaseDetails.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this UpdateAutonomousDatabaseDetails.
        Applies to dedicated Exadata infrastructure only.

        The size, in gigabytes, of the data volume that will be created and attached to the database. The maximum storage value depends on the system shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `dataStorageSizeInTBs` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this UpdateAutonomousDatabaseDetails.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateAutonomousDatabaseDetails.
        The user-friendly name for the Autonomous Database. The name does not have to be unique. The display name can only be updated for Autonomous Databases
        using dedicated Exadata infrastructure.


        :return: The display_name of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateAutonomousDatabaseDetails.
        The user-friendly name for the Autonomous Database. The name does not have to be unique. The display name can only be updated for Autonomous Databases
        using dedicated Exadata infrastructure.


        :param display_name: The display_name of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def is_free_tier(self):
        """
        Gets the is_free_tier of this UpdateAutonomousDatabaseDetails.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :return: The is_free_tier of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_free_tier

    @is_free_tier.setter
    def is_free_tier(self, is_free_tier):
        """
        Sets the is_free_tier of this UpdateAutonomousDatabaseDetails.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :param is_free_tier: The is_free_tier of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_free_tier = is_free_tier

    @property
    def admin_password(self):
        """
        Gets the admin_password of this UpdateAutonomousDatabaseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.


        :return: The admin_password of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._admin_password

    @admin_password.setter
    def admin_password(self, admin_password):
        """
        Sets the admin_password of this UpdateAutonomousDatabaseDetails.
        The password must be between 12 and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol (\") or the username \"admin\", regardless of casing. It must be different from the last four passwords and it must not be a password used within the last 24 hours.


        :param admin_password: The admin_password of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._admin_password = admin_password

    @property
    def db_name(self):
        """
        Gets the db_name of this UpdateAutonomousDatabaseDetails.
        New name for this Autonomous Database.
        For databases using dedicated Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.
        For databases using shared Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :return: The db_name of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this UpdateAutonomousDatabaseDetails.
        New name for this Autonomous Database.
        For databases using dedicated Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of eight alphanumeric characters. Special characters are not permitted.
        For databases using shared Exadata infrastructure, the name must begin with an alphabetic character, and can contain a maximum of 14 alphanumeric characters. Special characters are not permitted. The database name must be unique in the tenancy.


        :param db_name: The db_name of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._db_name = db_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateAutonomousDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this UpdateAutonomousDatabaseDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateAutonomousDatabaseDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this UpdateAutonomousDatabaseDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateAutonomousDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this UpdateAutonomousDatabaseDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateAutonomousDatabaseDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this UpdateAutonomousDatabaseDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def db_workload(self):
        """
        Gets the db_workload of this UpdateAutonomousDatabaseDetails.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.

        Allowed values for this property are: "OLTP", "DW", "AJD", "APEX"


        :return: The db_workload of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this UpdateAutonomousDatabaseDetails.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.


        :param db_workload: The db_workload of this UpdateAutonomousDatabaseDetails.
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
    def license_model(self):
        """
        Gets the license_model of this UpdateAutonomousDatabaseDetails.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"


        :return: The license_model of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this UpdateAutonomousDatabaseDetails.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param license_model: The license_model of this UpdateAutonomousDatabaseDetails.
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
    def is_access_control_enabled(self):
        """
        Gets the is_access_control_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates if the database-level access control is enabled.
        If disabled, database access is defined by the network security rules.
        If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,
         if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console.
        When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

        This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.


        :return: The is_access_control_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_access_control_enabled

    @is_access_control_enabled.setter
    def is_access_control_enabled(self, is_access_control_enabled):
        """
        Sets the is_access_control_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates if the database-level access control is enabled.
        If disabled, database access is defined by the network security rules.
        If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,
         if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console.
        When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

        This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.


        :param is_access_control_enabled: The is_access_control_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_access_control_enabled = is_access_control_enabled

    @property
    def whitelisted_ips(self):
        """
        Gets the whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :rtype: list[str]
        """
        return self._whitelisted_ips

    @whitelisted_ips.setter
    def whitelisted_ips(self, whitelisted_ips):
        """
        Sets the whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param whitelisted_ips: The whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :type: list[str]
        """
        self._whitelisted_ips = whitelisted_ips

    @property
    def are_primary_whitelisted_ips_used(self):
        """
        Gets the are_primary_whitelisted_ips_used of this UpdateAutonomousDatabaseDetails.
        This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
        `TRUE` if the Autonomous Database has Data Guard and Access Control enabled, and the Autonomous Database uses the primary's IP access control list (ACL) for standby.
        `FALSE` if the Autonomous Database has Data Guard and Access Control enabled, and the Autonomous Database uses a different IP access control list (ACL) for standby compared to primary.


        :return: The are_primary_whitelisted_ips_used of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._are_primary_whitelisted_ips_used

    @are_primary_whitelisted_ips_used.setter
    def are_primary_whitelisted_ips_used(self, are_primary_whitelisted_ips_used):
        """
        Sets the are_primary_whitelisted_ips_used of this UpdateAutonomousDatabaseDetails.
        This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
        `TRUE` if the Autonomous Database has Data Guard and Access Control enabled, and the Autonomous Database uses the primary's IP access control list (ACL) for standby.
        `FALSE` if the Autonomous Database has Data Guard and Access Control enabled, and the Autonomous Database uses a different IP access control list (ACL) for standby compared to primary.


        :param are_primary_whitelisted_ips_used: The are_primary_whitelisted_ips_used of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._are_primary_whitelisted_ips_used = are_primary_whitelisted_ips_used

    @property
    def standby_whitelisted_ips(self):
        """
        Gets the standby_whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The standby_whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :rtype: list[str]
        """
        return self._standby_whitelisted_ips

    @standby_whitelisted_ips.setter
    def standby_whitelisted_ips(self, standby_whitelisted_ips):
        """
        Sets the standby_whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param standby_whitelisted_ips: The standby_whitelisted_ips of this UpdateAutonomousDatabaseDetails.
        :type: list[str]
        """
        self._standby_whitelisted_ips = standby_whitelisted_ips

    @property
    def is_auto_scaling_enabled(self):
        """
        Gets the is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether auto scaling is enabled for the Autonomous Database OCPU core count. Setting to `TRUE` enables auto scaling. Setting to `FALSE` disables auto scaling. The default value is true. Auto scaling is available for databases on `shared Exadata infrastructure`__ only.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether auto scaling is enabled for the Autonomous Database OCPU core count. Setting to `TRUE` enables auto scaling. Setting to `FALSE` disables auto scaling. The default value is true. Auto scaling is available for databases on `shared Exadata infrastructure`__ only.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def is_refreshable_clone(self):
        """
        Gets the is_refreshable_clone of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database is a refreshable clone.


        :return: The is_refreshable_clone of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_refreshable_clone

    @is_refreshable_clone.setter
    def is_refreshable_clone(self, is_refreshable_clone):
        """
        Sets the is_refreshable_clone of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database is a refreshable clone.


        :param is_refreshable_clone: The is_refreshable_clone of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_refreshable_clone = is_refreshable_clone

    @property
    def refreshable_mode(self):
        """
        Gets the refreshable_mode of this UpdateAutonomousDatabaseDetails.
        The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.

        Allowed values for this property are: "AUTOMATIC", "MANUAL"


        :return: The refreshable_mode of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._refreshable_mode

    @refreshable_mode.setter
    def refreshable_mode(self, refreshable_mode):
        """
        Sets the refreshable_mode of this UpdateAutonomousDatabaseDetails.
        The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.


        :param refreshable_mode: The refreshable_mode of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        allowed_values = ["AUTOMATIC", "MANUAL"]
        if not value_allowed_none_or_none_sentinel(refreshable_mode, allowed_values):
            raise ValueError(
                "Invalid value for `refreshable_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._refreshable_mode = refreshable_mode

    @property
    def is_local_data_guard_enabled(self):
        """
        Gets the is_local_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable when creating a cross-region Autonomous Data Guard associations, or to
        Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

        To create a local standby, set to `TRUE`. To delete a local standby, set to `FALSE`. For more information on using Autonomous Data Guard on shared Exadata infrastructure (local and cross-region) , see `About Standby Databases`__

        To enable cross-region Autonomous Data Guard on shared Exadata infrastructure, see :func:`create_cross_region_autonomous_database_data_guard_details`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-data-guard-about.html#GUID-045AD017-8120-4BDC-AF58-7430FFE28D2B


        :return: The is_local_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_local_data_guard_enabled

    @is_local_data_guard_enabled.setter
    def is_local_data_guard_enabled(self, is_local_data_guard_enabled):
        """
        Sets the is_local_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable when creating a cross-region Autonomous Data Guard associations, or to
        Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

        To create a local standby, set to `TRUE`. To delete a local standby, set to `FALSE`. For more information on using Autonomous Data Guard on shared Exadata infrastructure (local and cross-region) , see `About Standby Databases`__

        To enable cross-region Autonomous Data Guard on shared Exadata infrastructure, see :func:`create_cross_region_autonomous_database_data_guard_details`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-data-guard-about.html#GUID-045AD017-8120-4BDC-AF58-7430FFE28D2B


        :param is_local_data_guard_enabled: The is_local_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_local_data_guard_enabled = is_local_data_guard_enabled

    @property
    def is_data_guard_enabled(self):
        """
        Gets the is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        ** Deprecated. ** Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable when creating a cross-region Autonomous Data Guard associations, or to
        Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

        To create a local standby, set to `TRUE`. To delete a local standby, set to `FALSE`. For more information on using Autonomous Data Guard on shared Exadata infrastructure (local and cross-region) , see `About Standby Databases`__

        To enable cross-region Autonomous Data Guard on shared Exadata infrastructure, see :func:`create_cross_region_autonomous_database_data_guard_details`.

        To delete a cross-region standby database, provide the `peerDbId` for the standby database in a remote region, and set `isDataGuardEnabled` to `FALSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-data-guard-about.html#GUID-045AD017-8120-4BDC-AF58-7430FFE28D2B


        :return: The is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_data_guard_enabled

    @is_data_guard_enabled.setter
    def is_data_guard_enabled(self, is_data_guard_enabled):
        """
        Sets the is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        ** Deprecated. ** Indicates whether the Autonomous Database has a local (in-region) standby database. Not applicable when creating a cross-region Autonomous Data Guard associations, or to
        Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.

        To create a local standby, set to `TRUE`. To delete a local standby, set to `FALSE`. For more information on using Autonomous Data Guard on shared Exadata infrastructure (local and cross-region) , see `About Standby Databases`__

        To enable cross-region Autonomous Data Guard on shared Exadata infrastructure, see :func:`create_cross_region_autonomous_database_data_guard_details`.

        To delete a cross-region standby database, provide the `peerDbId` for the standby database in a remote region, and set `isDataGuardEnabled` to `FALSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/autonomous-data-guard-about.html#GUID-045AD017-8120-4BDC-AF58-7430FFE28D2B


        :param is_data_guard_enabled: The is_data_guard_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_data_guard_enabled = is_data_guard_enabled

    @property
    def peer_db_id(self):
        """
        Gets the peer_db_id of this UpdateAutonomousDatabaseDetails.
        The `OCID`__ of the Autonomous Data Guard standby database located in a different (remote) region from the source primary Autonomous Database.

        To create or delete a local (in-region) standby, see the `isDataGuardEnabled` parameter.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_id of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._peer_db_id

    @peer_db_id.setter
    def peer_db_id(self, peer_db_id):
        """
        Sets the peer_db_id of this UpdateAutonomousDatabaseDetails.
        The `OCID`__ of the Autonomous Data Guard standby database located in a different (remote) region from the source primary Autonomous Database.

        To create or delete a local (in-region) standby, see the `isDataGuardEnabled` parameter.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_db_id: The peer_db_id of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._peer_db_id = peer_db_id

    @property
    def db_version(self):
        """
        Gets the db_version of this UpdateAutonomousDatabaseDetails.
        A valid Oracle Database version for Autonomous Database.


        :return: The db_version of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this UpdateAutonomousDatabaseDetails.
        A valid Oracle Database version for Autonomous Database.


        :param db_version: The db_version of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._db_version = db_version

    @property
    def open_mode(self):
        """
        Gets the open_mode of this UpdateAutonomousDatabaseDetails.
        The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.

        Allowed values for this property are: "READ_ONLY", "READ_WRITE"


        :return: The open_mode of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._open_mode

    @open_mode.setter
    def open_mode(self, open_mode):
        """
        Sets the open_mode of this UpdateAutonomousDatabaseDetails.
        The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.


        :param open_mode: The open_mode of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        allowed_values = ["READ_ONLY", "READ_WRITE"]
        if not value_allowed_none_or_none_sentinel(open_mode, allowed_values):
            raise ValueError(
                "Invalid value for `open_mode`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._open_mode = open_mode

    @property
    def permission_level(self):
        """
        Gets the permission_level of this UpdateAutonomousDatabaseDetails.
        The Autonomous Database permission level. Restricted mode allows access only to admin users.

        Allowed values for this property are: "RESTRICTED", "UNRESTRICTED"


        :return: The permission_level of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._permission_level

    @permission_level.setter
    def permission_level(self, permission_level):
        """
        Sets the permission_level of this UpdateAutonomousDatabaseDetails.
        The Autonomous Database permission level. Restricted mode allows access only to admin users.


        :param permission_level: The permission_level of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        allowed_values = ["RESTRICTED", "UNRESTRICTED"]
        if not value_allowed_none_or_none_sentinel(permission_level, allowed_values):
            raise ValueError(
                "Invalid value for `permission_level`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._permission_level = permission_level

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this UpdateAutonomousDatabaseDetails.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this UpdateAutonomousDatabaseDetails.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_label(self):
        """
        Gets the private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :return: The private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._private_endpoint_label

    @private_endpoint_label.setter
    def private_endpoint_label(self, private_endpoint_label):
        """
        Sets the private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :param private_endpoint_label: The private_endpoint_label of this UpdateAutonomousDatabaseDetails.
        :type: str
        """
        self._private_endpoint_label = private_endpoint_label

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this UpdateAutonomousDatabaseDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds list cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this UpdateAutonomousDatabaseDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this UpdateAutonomousDatabaseDetails.
        The list of `OCIDs`__ for the network security groups (NSGs) to which this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds list cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this UpdateAutonomousDatabaseDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def customer_contacts(self):
        """
        Gets the customer_contacts of this UpdateAutonomousDatabaseDetails.
        Customer Contacts. Setting this to an empty list removes all customer contacts of an Oracle Autonomous Database.


        :return: The customer_contacts of this UpdateAutonomousDatabaseDetails.
        :rtype: list[oci.database.models.CustomerContact]
        """
        return self._customer_contacts

    @customer_contacts.setter
    def customer_contacts(self, customer_contacts):
        """
        Sets the customer_contacts of this UpdateAutonomousDatabaseDetails.
        Customer Contacts. Setting this to an empty list removes all customer contacts of an Oracle Autonomous Database.


        :param customer_contacts: The customer_contacts of this UpdateAutonomousDatabaseDetails.
        :type: list[oci.database.models.CustomerContact]
        """
        self._customer_contacts = customer_contacts

    @property
    def is_mtls_connection_required(self):
        """
        Gets the is_mtls_connection_required of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database requires mTLS connections.


        :return: The is_mtls_connection_required of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_mtls_connection_required

    @is_mtls_connection_required.setter
    def is_mtls_connection_required(self, is_mtls_connection_required):
        """
        Sets the is_mtls_connection_required of this UpdateAutonomousDatabaseDetails.
        Indicates whether the Autonomous Database requires mTLS connections.


        :param is_mtls_connection_required: The is_mtls_connection_required of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_mtls_connection_required = is_mtls_connection_required

    @property
    def scheduled_operations(self):
        """
        Gets the scheduled_operations of this UpdateAutonomousDatabaseDetails.
        list of scheduled operations


        :return: The scheduled_operations of this UpdateAutonomousDatabaseDetails.
        :rtype: list[oci.database.models.ScheduledOperationDetails]
        """
        return self._scheduled_operations

    @scheduled_operations.setter
    def scheduled_operations(self, scheduled_operations):
        """
        Sets the scheduled_operations of this UpdateAutonomousDatabaseDetails.
        list of scheduled operations


        :param scheduled_operations: The scheduled_operations of this UpdateAutonomousDatabaseDetails.
        :type: list[oci.database.models.ScheduledOperationDetails]
        """
        self._scheduled_operations = scheduled_operations

    @property
    def is_auto_scaling_for_storage_enabled(self):
        """
        Gets the is_auto_scaling_for_storage_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.


        :return: The is_auto_scaling_for_storage_enabled of this UpdateAutonomousDatabaseDetails.
        :rtype: bool
        """
        return self._is_auto_scaling_for_storage_enabled

    @is_auto_scaling_for_storage_enabled.setter
    def is_auto_scaling_for_storage_enabled(self, is_auto_scaling_for_storage_enabled):
        """
        Sets the is_auto_scaling_for_storage_enabled of this UpdateAutonomousDatabaseDetails.
        Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.


        :param is_auto_scaling_for_storage_enabled: The is_auto_scaling_for_storage_enabled of this UpdateAutonomousDatabaseDetails.
        :type: bool
        """
        self._is_auto_scaling_for_storage_enabled = is_auto_scaling_for_storage_enabled

    @property
    def max_cpu_core_count(self):
        """
        Gets the max_cpu_core_count of this UpdateAutonomousDatabaseDetails.
        The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.


        :return: The max_cpu_core_count of this UpdateAutonomousDatabaseDetails.
        :rtype: int
        """
        return self._max_cpu_core_count

    @max_cpu_core_count.setter
    def max_cpu_core_count(self, max_cpu_core_count):
        """
        Sets the max_cpu_core_count of this UpdateAutonomousDatabaseDetails.
        The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.


        :param max_cpu_core_count: The max_cpu_core_count of this UpdateAutonomousDatabaseDetails.
        :type: int
        """
        self._max_cpu_core_count = max_cpu_core_count

    @property
    def database_edition(self):
        """
        Gets the database_edition of this UpdateAutonomousDatabaseDetails.
        The Oracle Database Edition that applies to the Autonomous databases.


        :return: The database_edition of this UpdateAutonomousDatabaseDetails.
        :rtype: str
        """
        return self._database_edition

    @database_edition.setter
    def database_edition(self, database_edition):
        """
        Sets the database_edition of this UpdateAutonomousDatabaseDetails.
        The Oracle Database Edition that applies to the Autonomous databases.


        :param database_edition: The database_edition of this UpdateAutonomousDatabaseDetails.
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
