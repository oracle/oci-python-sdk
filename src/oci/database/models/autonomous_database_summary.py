# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AutonomousDatabaseSummary(object):
    """
    An Oracle Autonomous Database.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "PROVISIONING"
    LIFECYCLE_STATE_PROVISIONING = "PROVISIONING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "AVAILABLE"
    LIFECYCLE_STATE_AVAILABLE = "AVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "TERMINATING"
    LIFECYCLE_STATE_TERMINATING = "TERMINATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "TERMINATED"
    LIFECYCLE_STATE_TERMINATED = "TERMINATED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "UNAVAILABLE"
    LIFECYCLE_STATE_UNAVAILABLE = "UNAVAILABLE"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "RESTORE_IN_PROGRESS"
    LIFECYCLE_STATE_RESTORE_IN_PROGRESS = "RESTORE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "RESTORE_FAILED"
    LIFECYCLE_STATE_RESTORE_FAILED = "RESTORE_FAILED"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "BACKUP_IN_PROGRESS"
    LIFECYCLE_STATE_BACKUP_IN_PROGRESS = "BACKUP_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "SCALE_IN_PROGRESS"
    LIFECYCLE_STATE_SCALE_IN_PROGRESS = "SCALE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "AVAILABLE_NEEDS_ATTENTION"
    LIFECYCLE_STATE_AVAILABLE_NEEDS_ATTENTION = "AVAILABLE_NEEDS_ATTENTION"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "MAINTENANCE_IN_PROGRESS"
    LIFECYCLE_STATE_MAINTENANCE_IN_PROGRESS = "MAINTENANCE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "RESTARTING"
    LIFECYCLE_STATE_RESTARTING = "RESTARTING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "RECREATING"
    LIFECYCLE_STATE_RECREATING = "RECREATING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "ROLE_CHANGE_IN_PROGRESS"
    LIFECYCLE_STATE_ROLE_CHANGE_IN_PROGRESS = "ROLE_CHANGE_IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "UPGRADING"
    LIFECYCLE_STATE_UPGRADING = "UPGRADING"

    #: A constant which can be used with the lifecycle_state property of a AutonomousDatabaseSummary.
    #: This constant has a value of "INACCESSIBLE"
    LIFECYCLE_STATE_INACCESSIBLE = "INACCESSIBLE"

    #: A constant which can be used with the infrastructure_type property of a AutonomousDatabaseSummary.
    #: This constant has a value of "CLOUD"
    INFRASTRUCTURE_TYPE_CLOUD = "CLOUD"

    #: A constant which can be used with the infrastructure_type property of a AutonomousDatabaseSummary.
    #: This constant has a value of "CLOUD_AT_CUSTOMER"
    INFRASTRUCTURE_TYPE_CLOUD_AT_CUSTOMER = "CLOUD_AT_CUSTOMER"

    #: A constant which can be used with the license_model property of a AutonomousDatabaseSummary.
    #: This constant has a value of "LICENSE_INCLUDED"
    LICENSE_MODEL_LICENSE_INCLUDED = "LICENSE_INCLUDED"

    #: A constant which can be used with the license_model property of a AutonomousDatabaseSummary.
    #: This constant has a value of "BRING_YOUR_OWN_LICENSE"
    LICENSE_MODEL_BRING_YOUR_OWN_LICENSE = "BRING_YOUR_OWN_LICENSE"

    #: A constant which can be used with the db_workload property of a AutonomousDatabaseSummary.
    #: This constant has a value of "OLTP"
    DB_WORKLOAD_OLTP = "OLTP"

    #: A constant which can be used with the db_workload property of a AutonomousDatabaseSummary.
    #: This constant has a value of "DW"
    DB_WORKLOAD_DW = "DW"

    #: A constant which can be used with the db_workload property of a AutonomousDatabaseSummary.
    #: This constant has a value of "AJD"
    DB_WORKLOAD_AJD = "AJD"

    #: A constant which can be used with the db_workload property of a AutonomousDatabaseSummary.
    #: This constant has a value of "APEX"
    DB_WORKLOAD_APEX = "APEX"

    #: A constant which can be used with the data_safe_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "REGISTERING"
    DATA_SAFE_STATUS_REGISTERING = "REGISTERING"

    #: A constant which can be used with the data_safe_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "REGISTERED"
    DATA_SAFE_STATUS_REGISTERED = "REGISTERED"

    #: A constant which can be used with the data_safe_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "DEREGISTERING"
    DATA_SAFE_STATUS_DEREGISTERING = "DEREGISTERING"

    #: A constant which can be used with the data_safe_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "NOT_REGISTERED"
    DATA_SAFE_STATUS_NOT_REGISTERED = "NOT_REGISTERED"

    #: A constant which can be used with the data_safe_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "FAILED"
    DATA_SAFE_STATUS_FAILED = "FAILED"

    #: A constant which can be used with the operations_insights_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "ENABLING"
    OPERATIONS_INSIGHTS_STATUS_ENABLING = "ENABLING"

    #: A constant which can be used with the operations_insights_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "ENABLED"
    OPERATIONS_INSIGHTS_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the operations_insights_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "DISABLING"
    OPERATIONS_INSIGHTS_STATUS_DISABLING = "DISABLING"

    #: A constant which can be used with the operations_insights_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "NOT_ENABLED"
    OPERATIONS_INSIGHTS_STATUS_NOT_ENABLED = "NOT_ENABLED"

    #: A constant which can be used with the operations_insights_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "FAILED_ENABLING"
    OPERATIONS_INSIGHTS_STATUS_FAILED_ENABLING = "FAILED_ENABLING"

    #: A constant which can be used with the operations_insights_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "FAILED_DISABLING"
    OPERATIONS_INSIGHTS_STATUS_FAILED_DISABLING = "FAILED_DISABLING"

    #: A constant which can be used with the database_management_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "ENABLING"
    DATABASE_MANAGEMENT_STATUS_ENABLING = "ENABLING"

    #: A constant which can be used with the database_management_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "ENABLED"
    DATABASE_MANAGEMENT_STATUS_ENABLED = "ENABLED"

    #: A constant which can be used with the database_management_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "DISABLING"
    DATABASE_MANAGEMENT_STATUS_DISABLING = "DISABLING"

    #: A constant which can be used with the database_management_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "NOT_ENABLED"
    DATABASE_MANAGEMENT_STATUS_NOT_ENABLED = "NOT_ENABLED"

    #: A constant which can be used with the database_management_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "FAILED_ENABLING"
    DATABASE_MANAGEMENT_STATUS_FAILED_ENABLING = "FAILED_ENABLING"

    #: A constant which can be used with the database_management_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "FAILED_DISABLING"
    DATABASE_MANAGEMENT_STATUS_FAILED_DISABLING = "FAILED_DISABLING"

    #: A constant which can be used with the open_mode property of a AutonomousDatabaseSummary.
    #: This constant has a value of "READ_ONLY"
    OPEN_MODE_READ_ONLY = "READ_ONLY"

    #: A constant which can be used with the open_mode property of a AutonomousDatabaseSummary.
    #: This constant has a value of "READ_WRITE"
    OPEN_MODE_READ_WRITE = "READ_WRITE"

    #: A constant which can be used with the refreshable_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "REFRESHING"
    REFRESHABLE_STATUS_REFRESHING = "REFRESHING"

    #: A constant which can be used with the refreshable_status property of a AutonomousDatabaseSummary.
    #: This constant has a value of "NOT_REFRESHING"
    REFRESHABLE_STATUS_NOT_REFRESHING = "NOT_REFRESHING"

    #: A constant which can be used with the refreshable_mode property of a AutonomousDatabaseSummary.
    #: This constant has a value of "AUTOMATIC"
    REFRESHABLE_MODE_AUTOMATIC = "AUTOMATIC"

    #: A constant which can be used with the refreshable_mode property of a AutonomousDatabaseSummary.
    #: This constant has a value of "MANUAL"
    REFRESHABLE_MODE_MANUAL = "MANUAL"

    #: A constant which can be used with the permission_level property of a AutonomousDatabaseSummary.
    #: This constant has a value of "RESTRICTED"
    PERMISSION_LEVEL_RESTRICTED = "RESTRICTED"

    #: A constant which can be used with the permission_level property of a AutonomousDatabaseSummary.
    #: This constant has a value of "UNRESTRICTED"
    PERMISSION_LEVEL_UNRESTRICTED = "UNRESTRICTED"

    #: A constant which can be used with the role property of a AutonomousDatabaseSummary.
    #: This constant has a value of "PRIMARY"
    ROLE_PRIMARY = "PRIMARY"

    #: A constant which can be used with the role property of a AutonomousDatabaseSummary.
    #: This constant has a value of "STANDBY"
    ROLE_STANDBY = "STANDBY"

    #: A constant which can be used with the role property of a AutonomousDatabaseSummary.
    #: This constant has a value of "DISABLED_STANDBY"
    ROLE_DISABLED_STANDBY = "DISABLED_STANDBY"

    #: A constant which can be used with the dataguard_region_type property of a AutonomousDatabaseSummary.
    #: This constant has a value of "PRIMARY_DG_REGION"
    DATAGUARD_REGION_TYPE_PRIMARY_DG_REGION = "PRIMARY_DG_REGION"

    #: A constant which can be used with the dataguard_region_type property of a AutonomousDatabaseSummary.
    #: This constant has a value of "REMOTE_STANDBY_DG_REGION"
    DATAGUARD_REGION_TYPE_REMOTE_STANDBY_DG_REGION = "REMOTE_STANDBY_DG_REGION"

    #: A constant which can be used with the autonomous_maintenance_schedule_type property of a AutonomousDatabaseSummary.
    #: This constant has a value of "EARLY"
    AUTONOMOUS_MAINTENANCE_SCHEDULE_TYPE_EARLY = "EARLY"

    #: A constant which can be used with the autonomous_maintenance_schedule_type property of a AutonomousDatabaseSummary.
    #: This constant has a value of "REGULAR"
    AUTONOMOUS_MAINTENANCE_SCHEDULE_TYPE_REGULAR = "REGULAR"

    def __init__(self, **kwargs):
        """
        Initializes a new AutonomousDatabaseSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AutonomousDatabaseSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this AutonomousDatabaseSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", "RESTARTING", "RECREATING", "ROLE_CHANGE_IN_PROGRESS", "UPGRADING", "INACCESSIBLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this AutonomousDatabaseSummary.
        :type lifecycle_details: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this AutonomousDatabaseSummary.
        :type kms_key_id: str

        :param vault_id:
            The value to assign to the vault_id property of this AutonomousDatabaseSummary.
        :type vault_id: str

        :param kms_key_lifecycle_details:
            The value to assign to the kms_key_lifecycle_details property of this AutonomousDatabaseSummary.
        :type kms_key_lifecycle_details: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this AutonomousDatabaseSummary.
        :type kms_key_version_id: str

        :param db_name:
            The value to assign to the db_name property of this AutonomousDatabaseSummary.
        :type db_name: str

        :param is_free_tier:
            The value to assign to the is_free_tier property of this AutonomousDatabaseSummary.
        :type is_free_tier: bool

        :param system_tags:
            The value to assign to the system_tags property of this AutonomousDatabaseSummary.
        :type system_tags: dict(str, dict(str, object))

        :param time_reclamation_of_free_autonomous_database:
            The value to assign to the time_reclamation_of_free_autonomous_database property of this AutonomousDatabaseSummary.
        :type time_reclamation_of_free_autonomous_database: datetime

        :param time_deletion_of_free_autonomous_database:
            The value to assign to the time_deletion_of_free_autonomous_database property of this AutonomousDatabaseSummary.
        :type time_deletion_of_free_autonomous_database: datetime

        :param backup_config:
            The value to assign to the backup_config property of this AutonomousDatabaseSummary.
        :type backup_config: oci.database.models.AutonomousDatabaseBackupConfig

        :param key_history_entry:
            The value to assign to the key_history_entry property of this AutonomousDatabaseSummary.
        :type key_history_entry: list[oci.database.models.AutonomousDatabaseKeyHistoryEntry]

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this AutonomousDatabaseSummary.
        :type cpu_core_count: int

        :param ocpu_count:
            The value to assign to the ocpu_count property of this AutonomousDatabaseSummary.
        :type ocpu_count: float

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this AutonomousDatabaseSummary.
        :type data_storage_size_in_tbs: int

        :param data_storage_size_in_gbs:
            The value to assign to the data_storage_size_in_gbs property of this AutonomousDatabaseSummary.
        :type data_storage_size_in_gbs: int

        :param infrastructure_type:
            The value to assign to the infrastructure_type property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "CLOUD", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type infrastructure_type: str

        :param is_dedicated:
            The value to assign to the is_dedicated property of this AutonomousDatabaseSummary.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this AutonomousDatabaseSummary.
        :type autonomous_container_database_id: str

        :param time_created:
            The value to assign to the time_created property of this AutonomousDatabaseSummary.
        :type time_created: datetime

        :param display_name:
            The value to assign to the display_name property of this AutonomousDatabaseSummary.
        :type display_name: str

        :param service_console_url:
            The value to assign to the service_console_url property of this AutonomousDatabaseSummary.
        :type service_console_url: str

        :param connection_strings:
            The value to assign to the connection_strings property of this AutonomousDatabaseSummary.
        :type connection_strings: oci.database.models.AutonomousDatabaseConnectionStrings

        :param connection_urls:
            The value to assign to the connection_urls property of this AutonomousDatabaseSummary.
        :type connection_urls: oci.database.models.AutonomousDatabaseConnectionUrls

        :param license_model:
            The value to assign to the license_model property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type license_model: str

        :param used_data_storage_size_in_tbs:
            The value to assign to the used_data_storage_size_in_tbs property of this AutonomousDatabaseSummary.
        :type used_data_storage_size_in_tbs: int

        :param freeform_tags:
            The value to assign to the freeform_tags property of this AutonomousDatabaseSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this AutonomousDatabaseSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param subnet_id:
            The value to assign to the subnet_id property of this AutonomousDatabaseSummary.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this AutonomousDatabaseSummary.
        :type nsg_ids: list[str]

        :param private_endpoint:
            The value to assign to the private_endpoint property of this AutonomousDatabaseSummary.
        :type private_endpoint: str

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this AutonomousDatabaseSummary.
        :type private_endpoint_label: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this AutonomousDatabaseSummary.
        :type private_endpoint_ip: str

        :param db_version:
            The value to assign to the db_version property of this AutonomousDatabaseSummary.
        :type db_version: str

        :param is_preview:
            The value to assign to the is_preview property of this AutonomousDatabaseSummary.
        :type is_preview: bool

        :param db_workload:
            The value to assign to the db_workload property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type db_workload: str

        :param is_access_control_enabled:
            The value to assign to the is_access_control_enabled property of this AutonomousDatabaseSummary.
        :type is_access_control_enabled: bool

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this AutonomousDatabaseSummary.
        :type whitelisted_ips: list[str]

        :param are_primary_whitelisted_ips_used:
            The value to assign to the are_primary_whitelisted_ips_used property of this AutonomousDatabaseSummary.
        :type are_primary_whitelisted_ips_used: bool

        :param standby_whitelisted_ips:
            The value to assign to the standby_whitelisted_ips property of this AutonomousDatabaseSummary.
        :type standby_whitelisted_ips: list[str]

        :param apex_details:
            The value to assign to the apex_details property of this AutonomousDatabaseSummary.
        :type apex_details: oci.database.models.AutonomousDatabaseApex

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this AutonomousDatabaseSummary.
        :type is_auto_scaling_enabled: bool

        :param data_safe_status:
            The value to assign to the data_safe_status property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "REGISTERING", "REGISTERED", "DEREGISTERING", "NOT_REGISTERED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type data_safe_status: str

        :param operations_insights_status:
            The value to assign to the operations_insights_status property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type operations_insights_status: str

        :param database_management_status:
            The value to assign to the database_management_status property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type database_management_status: str

        :param time_maintenance_begin:
            The value to assign to the time_maintenance_begin property of this AutonomousDatabaseSummary.
        :type time_maintenance_begin: datetime

        :param time_maintenance_end:
            The value to assign to the time_maintenance_end property of this AutonomousDatabaseSummary.
        :type time_maintenance_end: datetime

        :param is_refreshable_clone:
            The value to assign to the is_refreshable_clone property of this AutonomousDatabaseSummary.
        :type is_refreshable_clone: bool

        :param time_of_last_refresh:
            The value to assign to the time_of_last_refresh property of this AutonomousDatabaseSummary.
        :type time_of_last_refresh: datetime

        :param time_of_last_refresh_point:
            The value to assign to the time_of_last_refresh_point property of this AutonomousDatabaseSummary.
        :type time_of_last_refresh_point: datetime

        :param time_of_next_refresh:
            The value to assign to the time_of_next_refresh property of this AutonomousDatabaseSummary.
        :type time_of_next_refresh: datetime

        :param open_mode:
            The value to assign to the open_mode property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "READ_ONLY", "READ_WRITE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type open_mode: str

        :param refreshable_status:
            The value to assign to the refreshable_status property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "REFRESHING", "NOT_REFRESHING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type refreshable_status: str

        :param refreshable_mode:
            The value to assign to the refreshable_mode property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "AUTOMATIC", "MANUAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type refreshable_mode: str

        :param source_id:
            The value to assign to the source_id property of this AutonomousDatabaseSummary.
        :type source_id: str

        :param permission_level:
            The value to assign to the permission_level property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "RESTRICTED", "UNRESTRICTED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type permission_level: str

        :param time_of_last_switchover:
            The value to assign to the time_of_last_switchover property of this AutonomousDatabaseSummary.
        :type time_of_last_switchover: datetime

        :param time_of_last_failover:
            The value to assign to the time_of_last_failover property of this AutonomousDatabaseSummary.
        :type time_of_last_failover: datetime

        :param is_data_guard_enabled:
            The value to assign to the is_data_guard_enabled property of this AutonomousDatabaseSummary.
        :type is_data_guard_enabled: bool

        :param failed_data_recovery_in_seconds:
            The value to assign to the failed_data_recovery_in_seconds property of this AutonomousDatabaseSummary.
        :type failed_data_recovery_in_seconds: int

        :param standby_db:
            The value to assign to the standby_db property of this AutonomousDatabaseSummary.
        :type standby_db: oci.database.models.AutonomousDatabaseStandbySummary

        :param role:
            The value to assign to the role property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type role: str

        :param available_upgrade_versions:
            The value to assign to the available_upgrade_versions property of this AutonomousDatabaseSummary.
        :type available_upgrade_versions: list[str]

        :param key_store_id:
            The value to assign to the key_store_id property of this AutonomousDatabaseSummary.
        :type key_store_id: str

        :param key_store_wallet_name:
            The value to assign to the key_store_wallet_name property of this AutonomousDatabaseSummary.
        :type key_store_wallet_name: str

        :param supported_regions_to_clone_to:
            The value to assign to the supported_regions_to_clone_to property of this AutonomousDatabaseSummary.
        :type supported_regions_to_clone_to: list[str]

        :param customer_contacts:
            The value to assign to the customer_contacts property of this AutonomousDatabaseSummary.
        :type customer_contacts: list[oci.database.models.CustomerContact]

        :param time_local_data_guard_enabled:
            The value to assign to the time_local_data_guard_enabled property of this AutonomousDatabaseSummary.
        :type time_local_data_guard_enabled: datetime

        :param dataguard_region_type:
            The value to assign to the dataguard_region_type property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "PRIMARY_DG_REGION", "REMOTE_STANDBY_DG_REGION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type dataguard_region_type: str

        :param time_data_guard_role_changed:
            The value to assign to the time_data_guard_role_changed property of this AutonomousDatabaseSummary.
        :type time_data_guard_role_changed: datetime

        :param peer_db_ids:
            The value to assign to the peer_db_ids property of this AutonomousDatabaseSummary.
        :type peer_db_ids: list[str]

        :param is_mtls_connection_required:
            The value to assign to the is_mtls_connection_required property of this AutonomousDatabaseSummary.
        :type is_mtls_connection_required: bool

        :param is_reconnect_clone_enabled:
            The value to assign to the is_reconnect_clone_enabled property of this AutonomousDatabaseSummary.
        :type is_reconnect_clone_enabled: bool

        :param time_until_reconnect_clone_enabled:
            The value to assign to the time_until_reconnect_clone_enabled property of this AutonomousDatabaseSummary.
        :type time_until_reconnect_clone_enabled: datetime

        :param autonomous_maintenance_schedule_type:
            The value to assign to the autonomous_maintenance_schedule_type property of this AutonomousDatabaseSummary.
            Allowed values for this property are: "EARLY", "REGULAR", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type autonomous_maintenance_schedule_type: str

        :param scheduled_operations:
            The value to assign to the scheduled_operations property of this AutonomousDatabaseSummary.
        :type scheduled_operations: list[oci.database.models.ScheduledOperationDetails]

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'kms_key_id': 'str',
            'vault_id': 'str',
            'kms_key_lifecycle_details': 'str',
            'kms_key_version_id': 'str',
            'db_name': 'str',
            'is_free_tier': 'bool',
            'system_tags': 'dict(str, dict(str, object))',
            'time_reclamation_of_free_autonomous_database': 'datetime',
            'time_deletion_of_free_autonomous_database': 'datetime',
            'backup_config': 'AutonomousDatabaseBackupConfig',
            'key_history_entry': 'list[AutonomousDatabaseKeyHistoryEntry]',
            'cpu_core_count': 'int',
            'ocpu_count': 'float',
            'data_storage_size_in_tbs': 'int',
            'data_storage_size_in_gbs': 'int',
            'infrastructure_type': 'str',
            'is_dedicated': 'bool',
            'autonomous_container_database_id': 'str',
            'time_created': 'datetime',
            'display_name': 'str',
            'service_console_url': 'str',
            'connection_strings': 'AutonomousDatabaseConnectionStrings',
            'connection_urls': 'AutonomousDatabaseConnectionUrls',
            'license_model': 'str',
            'used_data_storage_size_in_tbs': 'int',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'private_endpoint': 'str',
            'private_endpoint_label': 'str',
            'private_endpoint_ip': 'str',
            'db_version': 'str',
            'is_preview': 'bool',
            'db_workload': 'str',
            'is_access_control_enabled': 'bool',
            'whitelisted_ips': 'list[str]',
            'are_primary_whitelisted_ips_used': 'bool',
            'standby_whitelisted_ips': 'list[str]',
            'apex_details': 'AutonomousDatabaseApex',
            'is_auto_scaling_enabled': 'bool',
            'data_safe_status': 'str',
            'operations_insights_status': 'str',
            'database_management_status': 'str',
            'time_maintenance_begin': 'datetime',
            'time_maintenance_end': 'datetime',
            'is_refreshable_clone': 'bool',
            'time_of_last_refresh': 'datetime',
            'time_of_last_refresh_point': 'datetime',
            'time_of_next_refresh': 'datetime',
            'open_mode': 'str',
            'refreshable_status': 'str',
            'refreshable_mode': 'str',
            'source_id': 'str',
            'permission_level': 'str',
            'time_of_last_switchover': 'datetime',
            'time_of_last_failover': 'datetime',
            'is_data_guard_enabled': 'bool',
            'failed_data_recovery_in_seconds': 'int',
            'standby_db': 'AutonomousDatabaseStandbySummary',
            'role': 'str',
            'available_upgrade_versions': 'list[str]',
            'key_store_id': 'str',
            'key_store_wallet_name': 'str',
            'supported_regions_to_clone_to': 'list[str]',
            'customer_contacts': 'list[CustomerContact]',
            'time_local_data_guard_enabled': 'datetime',
            'dataguard_region_type': 'str',
            'time_data_guard_role_changed': 'datetime',
            'peer_db_ids': 'list[str]',
            'is_mtls_connection_required': 'bool',
            'is_reconnect_clone_enabled': 'bool',
            'time_until_reconnect_clone_enabled': 'datetime',
            'autonomous_maintenance_schedule_type': 'str',
            'scheduled_operations': 'list[ScheduledOperationDetails]'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'kms_key_id': 'kmsKeyId',
            'vault_id': 'vaultId',
            'kms_key_lifecycle_details': 'kmsKeyLifecycleDetails',
            'kms_key_version_id': 'kmsKeyVersionId',
            'db_name': 'dbName',
            'is_free_tier': 'isFreeTier',
            'system_tags': 'systemTags',
            'time_reclamation_of_free_autonomous_database': 'timeReclamationOfFreeAutonomousDatabase',
            'time_deletion_of_free_autonomous_database': 'timeDeletionOfFreeAutonomousDatabase',
            'backup_config': 'backupConfig',
            'key_history_entry': 'keyHistoryEntry',
            'cpu_core_count': 'cpuCoreCount',
            'ocpu_count': 'ocpuCount',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'data_storage_size_in_gbs': 'dataStorageSizeInGBs',
            'infrastructure_type': 'infrastructureType',
            'is_dedicated': 'isDedicated',
            'autonomous_container_database_id': 'autonomousContainerDatabaseId',
            'time_created': 'timeCreated',
            'display_name': 'displayName',
            'service_console_url': 'serviceConsoleUrl',
            'connection_strings': 'connectionStrings',
            'connection_urls': 'connectionUrls',
            'license_model': 'licenseModel',
            'used_data_storage_size_in_tbs': 'usedDataStorageSizeInTBs',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'private_endpoint': 'privateEndpoint',
            'private_endpoint_label': 'privateEndpointLabel',
            'private_endpoint_ip': 'privateEndpointIp',
            'db_version': 'dbVersion',
            'is_preview': 'isPreview',
            'db_workload': 'dbWorkload',
            'is_access_control_enabled': 'isAccessControlEnabled',
            'whitelisted_ips': 'whitelistedIps',
            'are_primary_whitelisted_ips_used': 'arePrimaryWhitelistedIpsUsed',
            'standby_whitelisted_ips': 'standbyWhitelistedIps',
            'apex_details': 'apexDetails',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'data_safe_status': 'dataSafeStatus',
            'operations_insights_status': 'operationsInsightsStatus',
            'database_management_status': 'databaseManagementStatus',
            'time_maintenance_begin': 'timeMaintenanceBegin',
            'time_maintenance_end': 'timeMaintenanceEnd',
            'is_refreshable_clone': 'isRefreshableClone',
            'time_of_last_refresh': 'timeOfLastRefresh',
            'time_of_last_refresh_point': 'timeOfLastRefreshPoint',
            'time_of_next_refresh': 'timeOfNextRefresh',
            'open_mode': 'openMode',
            'refreshable_status': 'refreshableStatus',
            'refreshable_mode': 'refreshableMode',
            'source_id': 'sourceId',
            'permission_level': 'permissionLevel',
            'time_of_last_switchover': 'timeOfLastSwitchover',
            'time_of_last_failover': 'timeOfLastFailover',
            'is_data_guard_enabled': 'isDataGuardEnabled',
            'failed_data_recovery_in_seconds': 'failedDataRecoveryInSeconds',
            'standby_db': 'standbyDb',
            'role': 'role',
            'available_upgrade_versions': 'availableUpgradeVersions',
            'key_store_id': 'keyStoreId',
            'key_store_wallet_name': 'keyStoreWalletName',
            'supported_regions_to_clone_to': 'supportedRegionsToCloneTo',
            'customer_contacts': 'customerContacts',
            'time_local_data_guard_enabled': 'timeLocalDataGuardEnabled',
            'dataguard_region_type': 'dataguardRegionType',
            'time_data_guard_role_changed': 'timeDataGuardRoleChanged',
            'peer_db_ids': 'peerDbIds',
            'is_mtls_connection_required': 'isMtlsConnectionRequired',
            'is_reconnect_clone_enabled': 'isReconnectCloneEnabled',
            'time_until_reconnect_clone_enabled': 'timeUntilReconnectCloneEnabled',
            'autonomous_maintenance_schedule_type': 'autonomousMaintenanceScheduleType',
            'scheduled_operations': 'scheduledOperations'
        }

        self._id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._kms_key_id = None
        self._vault_id = None
        self._kms_key_lifecycle_details = None
        self._kms_key_version_id = None
        self._db_name = None
        self._is_free_tier = None
        self._system_tags = None
        self._time_reclamation_of_free_autonomous_database = None
        self._time_deletion_of_free_autonomous_database = None
        self._backup_config = None
        self._key_history_entry = None
        self._cpu_core_count = None
        self._ocpu_count = None
        self._data_storage_size_in_tbs = None
        self._data_storage_size_in_gbs = None
        self._infrastructure_type = None
        self._is_dedicated = None
        self._autonomous_container_database_id = None
        self._time_created = None
        self._display_name = None
        self._service_console_url = None
        self._connection_strings = None
        self._connection_urls = None
        self._license_model = None
        self._used_data_storage_size_in_tbs = None
        self._freeform_tags = None
        self._defined_tags = None
        self._subnet_id = None
        self._nsg_ids = None
        self._private_endpoint = None
        self._private_endpoint_label = None
        self._private_endpoint_ip = None
        self._db_version = None
        self._is_preview = None
        self._db_workload = None
        self._is_access_control_enabled = None
        self._whitelisted_ips = None
        self._are_primary_whitelisted_ips_used = None
        self._standby_whitelisted_ips = None
        self._apex_details = None
        self._is_auto_scaling_enabled = None
        self._data_safe_status = None
        self._operations_insights_status = None
        self._database_management_status = None
        self._time_maintenance_begin = None
        self._time_maintenance_end = None
        self._is_refreshable_clone = None
        self._time_of_last_refresh = None
        self._time_of_last_refresh_point = None
        self._time_of_next_refresh = None
        self._open_mode = None
        self._refreshable_status = None
        self._refreshable_mode = None
        self._source_id = None
        self._permission_level = None
        self._time_of_last_switchover = None
        self._time_of_last_failover = None
        self._is_data_guard_enabled = None
        self._failed_data_recovery_in_seconds = None
        self._standby_db = None
        self._role = None
        self._available_upgrade_versions = None
        self._key_store_id = None
        self._key_store_wallet_name = None
        self._supported_regions_to_clone_to = None
        self._customer_contacts = None
        self._time_local_data_guard_enabled = None
        self._dataguard_region_type = None
        self._time_data_guard_role_changed = None
        self._peer_db_ids = None
        self._is_mtls_connection_required = None
        self._is_reconnect_clone_enabled = None
        self._time_until_reconnect_clone_enabled = None
        self._autonomous_maintenance_schedule_type = None
        self._scheduled_operations = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AutonomousDatabaseSummary.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutonomousDatabaseSummary.
        The `OCID`__ of the Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this AutonomousDatabaseSummary.
        The current state of the Autonomous Database.

        Allowed values for this property are: "PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", "RESTARTING", "RECREATING", "ROLE_CHANGE_IN_PROGRESS", "UPGRADING", "INACCESSIBLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this AutonomousDatabaseSummary.
        The current state of the Autonomous Database.


        :param lifecycle_state: The lifecycle_state of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["PROVISIONING", "AVAILABLE", "STOPPING", "STOPPED", "STARTING", "TERMINATING", "TERMINATED", "UNAVAILABLE", "RESTORE_IN_PROGRESS", "RESTORE_FAILED", "BACKUP_IN_PROGRESS", "SCALE_IN_PROGRESS", "AVAILABLE_NEEDS_ATTENTION", "UPDATING", "MAINTENANCE_IN_PROGRESS", "RESTARTING", "RECREATING", "ROLE_CHANGE_IN_PROGRESS", "UPGRADING", "INACCESSIBLE"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this AutonomousDatabaseSummary.
        Information about the current lifecycle state.


        :return: The lifecycle_details of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this AutonomousDatabaseSummary.
        Information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this AutonomousDatabaseSummary.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def kms_key_id(self):
        """
        Gets the kms_key_id of this AutonomousDatabaseSummary.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :return: The kms_key_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """
        Sets the kms_key_id of this AutonomousDatabaseSummary.
        The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.


        :param kms_key_id: The kms_key_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._kms_key_id = kms_key_id

    @property
    def vault_id(self):
        """
        Gets the vault_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :return: The vault_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._vault_id

    @vault_id.setter
    def vault_id(self, vault_id):
        """
        Sets the vault_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the Oracle Cloud Infrastructure `vault`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts


        :param vault_id: The vault_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._vault_id = vault_id

    @property
    def kms_key_lifecycle_details(self):
        """
        Gets the kms_key_lifecycle_details of this AutonomousDatabaseSummary.
        KMS key lifecycle details.


        :return: The kms_key_lifecycle_details of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._kms_key_lifecycle_details

    @kms_key_lifecycle_details.setter
    def kms_key_lifecycle_details(self, kms_key_lifecycle_details):
        """
        Sets the kms_key_lifecycle_details of this AutonomousDatabaseSummary.
        KMS key lifecycle details.


        :param kms_key_lifecycle_details: The kms_key_lifecycle_details of this AutonomousDatabaseSummary.
        :type: str
        """
        self._kms_key_lifecycle_details = kms_key_lifecycle_details

    @property
    def kms_key_version_id(self):
        """
        Gets the kms_key_version_id of this AutonomousDatabaseSummary.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :return: The kms_key_version_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._kms_key_version_id

    @kms_key_version_id.setter
    def kms_key_version_id(self, kms_key_version_id):
        """
        Sets the kms_key_version_id of this AutonomousDatabaseSummary.
        The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.


        :param kms_key_version_id: The kms_key_version_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._kms_key_version_id = kms_key_version_id

    @property
    def db_name(self):
        """
        **[Required]** Gets the db_name of this AutonomousDatabaseSummary.
        The database name.


        :return: The db_name of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._db_name

    @db_name.setter
    def db_name(self, db_name):
        """
        Sets the db_name of this AutonomousDatabaseSummary.
        The database name.


        :param db_name: The db_name of this AutonomousDatabaseSummary.
        :type: str
        """
        self._db_name = db_name

    @property
    def is_free_tier(self):
        """
        Gets the is_free_tier of this AutonomousDatabaseSummary.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :return: The is_free_tier of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_free_tier

    @is_free_tier.setter
    def is_free_tier(self, is_free_tier):
        """
        Sets the is_free_tier of this AutonomousDatabaseSummary.
        Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of memory. For Always Free databases, memory and CPU cannot be scaled.


        :param is_free_tier: The is_free_tier of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_free_tier = is_free_tier

    @property
    def system_tags(self):
        """
        Gets the system_tags of this AutonomousDatabaseSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The system_tags of this AutonomousDatabaseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this AutonomousDatabaseSummary.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param system_tags: The system_tags of this AutonomousDatabaseSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def time_reclamation_of_free_autonomous_database(self):
        """
        Gets the time_reclamation_of_free_autonomous_database of this AutonomousDatabaseSummary.
        The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the database will automatically be put into the STOPPED state.


        :return: The time_reclamation_of_free_autonomous_database of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_reclamation_of_free_autonomous_database

    @time_reclamation_of_free_autonomous_database.setter
    def time_reclamation_of_free_autonomous_database(self, time_reclamation_of_free_autonomous_database):
        """
        Sets the time_reclamation_of_free_autonomous_database of this AutonomousDatabaseSummary.
        The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the database will automatically be put into the STOPPED state.


        :param time_reclamation_of_free_autonomous_database: The time_reclamation_of_free_autonomous_database of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_reclamation_of_free_autonomous_database = time_reclamation_of_free_autonomous_database

    @property
    def time_deletion_of_free_autonomous_database(self):
        """
        Gets the time_deletion_of_free_autonomous_database of this AutonomousDatabaseSummary.
        The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and without activity until this time, it will be deleted.


        :return: The time_deletion_of_free_autonomous_database of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_deletion_of_free_autonomous_database

    @time_deletion_of_free_autonomous_database.setter
    def time_deletion_of_free_autonomous_database(self, time_deletion_of_free_autonomous_database):
        """
        Sets the time_deletion_of_free_autonomous_database of this AutonomousDatabaseSummary.
        The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and without activity until this time, it will be deleted.


        :param time_deletion_of_free_autonomous_database: The time_deletion_of_free_autonomous_database of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_deletion_of_free_autonomous_database = time_deletion_of_free_autonomous_database

    @property
    def backup_config(self):
        """
        Gets the backup_config of this AutonomousDatabaseSummary.

        :return: The backup_config of this AutonomousDatabaseSummary.
        :rtype: oci.database.models.AutonomousDatabaseBackupConfig
        """
        return self._backup_config

    @backup_config.setter
    def backup_config(self, backup_config):
        """
        Sets the backup_config of this AutonomousDatabaseSummary.

        :param backup_config: The backup_config of this AutonomousDatabaseSummary.
        :type: oci.database.models.AutonomousDatabaseBackupConfig
        """
        self._backup_config = backup_config

    @property
    def key_history_entry(self):
        """
        Gets the key_history_entry of this AutonomousDatabaseSummary.
        Key History Entry.


        :return: The key_history_entry of this AutonomousDatabaseSummary.
        :rtype: list[oci.database.models.AutonomousDatabaseKeyHistoryEntry]
        """
        return self._key_history_entry

    @key_history_entry.setter
    def key_history_entry(self, key_history_entry):
        """
        Sets the key_history_entry of this AutonomousDatabaseSummary.
        Key History Entry.


        :param key_history_entry: The key_history_entry of this AutonomousDatabaseSummary.
        :type: list[oci.database.models.AutonomousDatabaseKeyHistoryEntry]
        """
        self._key_history_entry = key_history_entry

    @property
    def cpu_core_count(self):
        """
        **[Required]** Gets the cpu_core_count of this AutonomousDatabaseSummary.
        The number of OCPU cores to be made available to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `ocpuCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The cpu_core_count of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._cpu_core_count

    @cpu_core_count.setter
    def cpu_core_count(self, cpu_core_count):
        """
        Sets the cpu_core_count of this AutonomousDatabaseSummary.
        The number of OCPU cores to be made available to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `ocpuCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param cpu_core_count: The cpu_core_count of this AutonomousDatabaseSummary.
        :type: int
        """
        self._cpu_core_count = cpu_core_count

    @property
    def ocpu_count(self):
        """
        Gets the ocpu_count of this AutonomousDatabaseSummary.
        The number of OCPU cores to be made available to the database.

        The following points apply:
        - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Databasese on shared Exadata infrastructure.)
        - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata infrastructure.

        For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :return: The ocpu_count of this AutonomousDatabaseSummary.
        :rtype: float
        """
        return self._ocpu_count

    @ocpu_count.setter
    def ocpu_count(self, ocpu_count):
        """
        Sets the ocpu_count of this AutonomousDatabaseSummary.
        The number of OCPU cores to be made available to the database.

        The following points apply:
        - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous Databasese on shared Exadata infrastructure.)
        - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata infrastructure.

        For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See `Characteristics of Infrastructure Shapes`__ for shape details.

        **Note:** This parameter cannot be used with the `cpuCoreCount` parameter.

        __ https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1


        :param ocpu_count: The ocpu_count of this AutonomousDatabaseSummary.
        :type: float
        """
        self._ocpu_count = ocpu_count

    @property
    def data_storage_size_in_tbs(self):
        """
        **[Required]** Gets the data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The quantity of data in the database, in terabytes.


        :return: The data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._data_storage_size_in_tbs

    @data_storage_size_in_tbs.setter
    def data_storage_size_in_tbs(self, data_storage_size_in_tbs):
        """
        Sets the data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The quantity of data in the database, in terabytes.


        :param data_storage_size_in_tbs: The data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :type: int
        """
        self._data_storage_size_in_tbs = data_storage_size_in_tbs

    @property
    def data_storage_size_in_gbs(self):
        """
        Gets the data_storage_size_in_gbs of this AutonomousDatabaseSummary.
        The quantity of data in the database, in gigabytes.


        :return: The data_storage_size_in_gbs of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._data_storage_size_in_gbs

    @data_storage_size_in_gbs.setter
    def data_storage_size_in_gbs(self, data_storage_size_in_gbs):
        """
        Sets the data_storage_size_in_gbs of this AutonomousDatabaseSummary.
        The quantity of data in the database, in gigabytes.


        :param data_storage_size_in_gbs: The data_storage_size_in_gbs of this AutonomousDatabaseSummary.
        :type: int
        """
        self._data_storage_size_in_gbs = data_storage_size_in_gbs

    @property
    def infrastructure_type(self):
        """
        Gets the infrastructure_type of this AutonomousDatabaseSummary.
        The infrastructure type this resource belongs to.

        Allowed values for this property are: "CLOUD", "CLOUD_AT_CUSTOMER", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The infrastructure_type of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._infrastructure_type

    @infrastructure_type.setter
    def infrastructure_type(self, infrastructure_type):
        """
        Sets the infrastructure_type of this AutonomousDatabaseSummary.
        The infrastructure type this resource belongs to.


        :param infrastructure_type: The infrastructure_type of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["CLOUD", "CLOUD_AT_CUSTOMER"]
        if not value_allowed_none_or_none_sentinel(infrastructure_type, allowed_values):
            infrastructure_type = 'UNKNOWN_ENUM_VALUE'
        self._infrastructure_type = infrastructure_type

    @property
    def is_dedicated(self):
        """
        Gets the is_dedicated of this AutonomousDatabaseSummary.
        True if the database uses `dedicated Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The is_dedicated of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_dedicated

    @is_dedicated.setter
    def is_dedicated(self, is_dedicated):
        """
        Sets the is_dedicated of this AutonomousDatabaseSummary.
        True if the database uses `dedicated Exadata infrastructure`__.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param is_dedicated: The is_dedicated of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_dedicated = is_dedicated

    @property
    def autonomous_container_database_id(self):
        """
        Gets the autonomous_container_database_id of this AutonomousDatabaseSummary.
        The Autonomous Container Database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_container_database_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._autonomous_container_database_id

    @autonomous_container_database_id.setter
    def autonomous_container_database_id(self, autonomous_container_database_id):
        """
        Sets the autonomous_container_database_id of this AutonomousDatabaseSummary.
        The Autonomous Container Database `OCID`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_container_database_id: The autonomous_container_database_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._autonomous_container_database_id = autonomous_container_database_id

    @property
    def time_created(self):
        """
        Gets the time_created of this AutonomousDatabaseSummary.
        The date and time the Autonomous Database was created.


        :return: The time_created of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this AutonomousDatabaseSummary.
        The date and time the Autonomous Database was created.


        :param time_created: The time_created of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def display_name(self):
        """
        Gets the display_name of this AutonomousDatabaseSummary.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :return: The display_name of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this AutonomousDatabaseSummary.
        The user-friendly name for the Autonomous Database. The name does not have to be unique.


        :param display_name: The display_name of this AutonomousDatabaseSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def service_console_url(self):
        """
        Gets the service_console_url of this AutonomousDatabaseSummary.
        The URL of the Service Console for the Autonomous Database.


        :return: The service_console_url of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._service_console_url

    @service_console_url.setter
    def service_console_url(self, service_console_url):
        """
        Sets the service_console_url of this AutonomousDatabaseSummary.
        The URL of the Service Console for the Autonomous Database.


        :param service_console_url: The service_console_url of this AutonomousDatabaseSummary.
        :type: str
        """
        self._service_console_url = service_console_url

    @property
    def connection_strings(self):
        """
        Gets the connection_strings of this AutonomousDatabaseSummary.
        The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.


        :return: The connection_strings of this AutonomousDatabaseSummary.
        :rtype: oci.database.models.AutonomousDatabaseConnectionStrings
        """
        return self._connection_strings

    @connection_strings.setter
    def connection_strings(self, connection_strings):
        """
        Sets the connection_strings of this AutonomousDatabaseSummary.
        The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered when creating the Autonomous Database for the password value.


        :param connection_strings: The connection_strings of this AutonomousDatabaseSummary.
        :type: oci.database.models.AutonomousDatabaseConnectionStrings
        """
        self._connection_strings = connection_strings

    @property
    def connection_urls(self):
        """
        Gets the connection_urls of this AutonomousDatabaseSummary.

        :return: The connection_urls of this AutonomousDatabaseSummary.
        :rtype: oci.database.models.AutonomousDatabaseConnectionUrls
        """
        return self._connection_urls

    @connection_urls.setter
    def connection_urls(self, connection_urls):
        """
        Sets the connection_urls of this AutonomousDatabaseSummary.

        :param connection_urls: The connection_urls of this AutonomousDatabaseSummary.
        :type: oci.database.models.AutonomousDatabaseConnectionUrls
        """
        self._connection_urls = connection_urls

    @property
    def license_model(self):
        """
        Gets the license_model of this AutonomousDatabaseSummary.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html

        Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The license_model of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._license_model

    @license_model.setter
    def license_model(self, license_model):
        """
        Sets the license_model of this AutonomousDatabaseSummary.
        The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
        License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
        Note that when provisioning an Autonomous Database on `dedicated Exadata infrastructure`__, this attribute must be null because the attribute is already set at the
        Autonomous Exadata Infrastructure level. When using `shared Exadata infrastructure`__, if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html
        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param license_model: The license_model of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
        if not value_allowed_none_or_none_sentinel(license_model, allowed_values):
            license_model = 'UNKNOWN_ENUM_VALUE'
        self._license_model = license_model

    @property
    def used_data_storage_size_in_tbs(self):
        """
        Gets the used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The amount of storage that has been used, in terabytes.


        :return: The used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._used_data_storage_size_in_tbs

    @used_data_storage_size_in_tbs.setter
    def used_data_storage_size_in_tbs(self, used_data_storage_size_in_tbs):
        """
        Sets the used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        The amount of storage that has been used, in terabytes.


        :param used_data_storage_size_in_tbs: The used_data_storage_size_in_tbs of this AutonomousDatabaseSummary.
        :type: int
        """
        self._used_data_storage_size_in_tbs = used_data_storage_size_in_tbs

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this AutonomousDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this AutonomousDatabaseSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this AutonomousDatabaseSummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this AutonomousDatabaseSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this AutonomousDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this AutonomousDatabaseSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this AutonomousDatabaseSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this AutonomousDatabaseSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the subnet the resource is associated with.

        **Subnet Restrictions:**
        - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
        - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
        - For Autonomous Database, setting this will disable public secure access to the database.

        These subnets are used by the Oracle Clusterware private interconnect on the database instance.
        Specifying an overlapping subnet will cause the private interconnect to malfunction.
        This restriction applies to both the client subnet and the backup subnet.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this AutonomousDatabaseSummary.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :return: The nsg_ids of this AutonomousDatabaseSummary.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this AutonomousDatabaseSummary.
        A list of the `OCIDs`__ of the network security groups (NSGs) that this resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs, see `Security Rules`__.
        **NsgIds restrictions:**
        - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm


        :param nsg_ids: The nsg_ids of this AutonomousDatabaseSummary.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def private_endpoint(self):
        """
        Gets the private_endpoint of this AutonomousDatabaseSummary.
        The private endpoint for the resource.


        :return: The private_endpoint of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._private_endpoint

    @private_endpoint.setter
    def private_endpoint(self, private_endpoint):
        """
        Sets the private_endpoint of this AutonomousDatabaseSummary.
        The private endpoint for the resource.


        :param private_endpoint: The private_endpoint of this AutonomousDatabaseSummary.
        :type: str
        """
        self._private_endpoint = private_endpoint

    @property
    def private_endpoint_label(self):
        """
        Gets the private_endpoint_label of this AutonomousDatabaseSummary.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :return: The private_endpoint_label of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._private_endpoint_label

    @private_endpoint_label.setter
    def private_endpoint_label(self, private_endpoint_label):
        """
        Sets the private_endpoint_label of this AutonomousDatabaseSummary.
        The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the same private endpoint database to the public endpoint database.


        :param private_endpoint_label: The private_endpoint_label of this AutonomousDatabaseSummary.
        :type: str
        """
        self._private_endpoint_label = private_endpoint_label

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this AutonomousDatabaseSummary.
        The private endpoint Ip address for the resource.


        :return: The private_endpoint_ip of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this AutonomousDatabaseSummary.
        The private endpoint Ip address for the resource.


        :param private_endpoint_ip: The private_endpoint_ip of this AutonomousDatabaseSummary.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def db_version(self):
        """
        Gets the db_version of this AutonomousDatabaseSummary.
        A valid Oracle Database version for Autonomous Database.


        :return: The db_version of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._db_version

    @db_version.setter
    def db_version(self, db_version):
        """
        Sets the db_version of this AutonomousDatabaseSummary.
        A valid Oracle Database version for Autonomous Database.


        :param db_version: The db_version of this AutonomousDatabaseSummary.
        :type: str
        """
        self._db_version = db_version

    @property
    def is_preview(self):
        """
        Gets the is_preview of this AutonomousDatabaseSummary.
        Indicates if the Autonomous Database version is a preview version.


        :return: The is_preview of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_preview

    @is_preview.setter
    def is_preview(self, is_preview):
        """
        Sets the is_preview of this AutonomousDatabaseSummary.
        Indicates if the Autonomous Database version is a preview version.


        :param is_preview: The is_preview of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_preview = is_preview

    @property
    def db_workload(self):
        """
        Gets the db_workload of this AutonomousDatabaseSummary.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.

        Allowed values for this property are: "OLTP", "DW", "AJD", "APEX", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The db_workload of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._db_workload

    @db_workload.setter
    def db_workload(self, db_workload):
        """
        Sets the db_workload of this AutonomousDatabaseSummary.
        The Autonomous Database workload type. The following values are valid:

        - OLTP - indicates an Autonomous Transaction Processing database
        - DW - indicates an Autonomous Data Warehouse database
        - AJD - indicates an Autonomous JSON Database
        - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type.


        :param db_workload: The db_workload of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["OLTP", "DW", "AJD", "APEX"]
        if not value_allowed_none_or_none_sentinel(db_workload, allowed_values):
            db_workload = 'UNKNOWN_ENUM_VALUE'
        self._db_workload = db_workload

    @property
    def is_access_control_enabled(self):
        """
        Gets the is_access_control_enabled of this AutonomousDatabaseSummary.
        Indicates if the database-level access control is enabled.
        If disabled, database access is defined by the network security rules.
        If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,
         if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console.
        When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

        This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.


        :return: The is_access_control_enabled of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_access_control_enabled

    @is_access_control_enabled.setter
    def is_access_control_enabled(self, is_access_control_enabled):
        """
        Sets the is_access_control_enabled of this AutonomousDatabaseSummary.
        Indicates if the database-level access control is enabled.
        If disabled, database access is defined by the network security rules.
        If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying `whitelistedIps` rules is optional,
         if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using the `UpdateAutonomousDatabase` API operation or edit option in console.
        When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled for the clone.

        This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.


        :param is_access_control_enabled: The is_access_control_enabled of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_access_control_enabled = is_access_control_enabled

    @property
    def whitelisted_ips(self):
        """
        Gets the whitelisted_ips of this AutonomousDatabaseSummary.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The whitelisted_ips of this AutonomousDatabaseSummary.
        :rtype: list[str]
        """
        return self._whitelisted_ips

    @whitelisted_ips.setter
    def whitelisted_ips(self, whitelisted_ips):
        """
        Sets the whitelisted_ips of this AutonomousDatabaseSummary.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param whitelisted_ips: The whitelisted_ips of this AutonomousDatabaseSummary.
        :type: list[str]
        """
        self._whitelisted_ips = whitelisted_ips

    @property
    def are_primary_whitelisted_ips_used(self):
        """
        Gets the are_primary_whitelisted_ips_used of this AutonomousDatabaseSummary.
        This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
        It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby.
        It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.


        :return: The are_primary_whitelisted_ips_used of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._are_primary_whitelisted_ips_used

    @are_primary_whitelisted_ips_used.setter
    def are_primary_whitelisted_ips_used(self, are_primary_whitelisted_ips_used):
        """
        Sets the are_primary_whitelisted_ips_used of this AutonomousDatabaseSummary.
        This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
        It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary IP access control list (ACL) for standby.
        It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses different IP access control list (ACL) for standby compared to primary.


        :param are_primary_whitelisted_ips_used: The are_primary_whitelisted_ips_used of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._are_primary_whitelisted_ips_used = are_primary_whitelisted_ips_used

    @property
    def standby_whitelisted_ips(self):
        """
        Gets the standby_whitelisted_ips of this AutonomousDatabaseSummary.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :return: The standby_whitelisted_ips of this AutonomousDatabaseSummary.
        :rtype: list[str]
        """
        return self._standby_whitelisted_ips

    @standby_whitelisted_ips.setter
    def standby_whitelisted_ips(self, standby_whitelisted_ips):
        """
        Sets the standby_whitelisted_ips of this AutonomousDatabaseSummary.
        The client IP access control list (ACL). This feature is available for autonomous databases on `shared Exadata infrastructure`__ and on Exadata Cloud@Customer.
        Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.

        For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
        Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"ocid1.vcn.oc1.sea.<unique_id>\",\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\",\"ocid1.vcn.oc1.sea.<unique_id2>;1.1.0.0/16\"]`
        For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
        Example: `[\"1.1.1.1\",\"1.1.1.0/24\",\"1.1.2.25\"]`

        For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.

        __ https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html


        :param standby_whitelisted_ips: The standby_whitelisted_ips of this AutonomousDatabaseSummary.
        :type: list[str]
        """
        self._standby_whitelisted_ips = standby_whitelisted_ips

    @property
    def apex_details(self):
        """
        Gets the apex_details of this AutonomousDatabaseSummary.
        Information about Oracle APEX Application Development.


        :return: The apex_details of this AutonomousDatabaseSummary.
        :rtype: oci.database.models.AutonomousDatabaseApex
        """
        return self._apex_details

    @apex_details.setter
    def apex_details(self, apex_details):
        """
        Sets the apex_details of this AutonomousDatabaseSummary.
        Information about Oracle APEX Application Development.


        :param apex_details: The apex_details of this AutonomousDatabaseSummary.
        :type: oci.database.models.AutonomousDatabaseApex
        """
        self._apex_details = apex_details

    @property
    def is_auto_scaling_enabled(self):
        """
        Gets the is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        Indicates if auto scaling is enabled for the Autonomous Database CPU core count.


        :return: The is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_auto_scaling_enabled

    @is_auto_scaling_enabled.setter
    def is_auto_scaling_enabled(self, is_auto_scaling_enabled):
        """
        Sets the is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        Indicates if auto scaling is enabled for the Autonomous Database CPU core count.


        :param is_auto_scaling_enabled: The is_auto_scaling_enabled of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_auto_scaling_enabled = is_auto_scaling_enabled

    @property
    def data_safe_status(self):
        """
        Gets the data_safe_status of this AutonomousDatabaseSummary.
        Status of the Data Safe registration for this Autonomous Database.

        Allowed values for this property are: "REGISTERING", "REGISTERED", "DEREGISTERING", "NOT_REGISTERED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The data_safe_status of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._data_safe_status

    @data_safe_status.setter
    def data_safe_status(self, data_safe_status):
        """
        Sets the data_safe_status of this AutonomousDatabaseSummary.
        Status of the Data Safe registration for this Autonomous Database.


        :param data_safe_status: The data_safe_status of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["REGISTERING", "REGISTERED", "DEREGISTERING", "NOT_REGISTERED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(data_safe_status, allowed_values):
            data_safe_status = 'UNKNOWN_ENUM_VALUE'
        self._data_safe_status = data_safe_status

    @property
    def operations_insights_status(self):
        """
        Gets the operations_insights_status of this AutonomousDatabaseSummary.
        Status of Operations Insights for this Autonomous Database.

        Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The operations_insights_status of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._operations_insights_status

    @operations_insights_status.setter
    def operations_insights_status(self, operations_insights_status):
        """
        Sets the operations_insights_status of this AutonomousDatabaseSummary.
        Status of Operations Insights for this Autonomous Database.


        :param operations_insights_status: The operations_insights_status of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING"]
        if not value_allowed_none_or_none_sentinel(operations_insights_status, allowed_values):
            operations_insights_status = 'UNKNOWN_ENUM_VALUE'
        self._operations_insights_status = operations_insights_status

    @property
    def database_management_status(self):
        """
        Gets the database_management_status of this AutonomousDatabaseSummary.
        Status of Database Management for this Autonomous Database.

        Allowed values for this property are: "ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The database_management_status of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._database_management_status

    @database_management_status.setter
    def database_management_status(self, database_management_status):
        """
        Sets the database_management_status of this AutonomousDatabaseSummary.
        Status of Database Management for this Autonomous Database.


        :param database_management_status: The database_management_status of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["ENABLING", "ENABLED", "DISABLING", "NOT_ENABLED", "FAILED_ENABLING", "FAILED_DISABLING"]
        if not value_allowed_none_or_none_sentinel(database_management_status, allowed_values):
            database_management_status = 'UNKNOWN_ENUM_VALUE'
        self._database_management_status = database_management_status

    @property
    def time_maintenance_begin(self):
        """
        Gets the time_maintenance_begin of this AutonomousDatabaseSummary.
        The date and time when maintenance will begin.


        :return: The time_maintenance_begin of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_maintenance_begin

    @time_maintenance_begin.setter
    def time_maintenance_begin(self, time_maintenance_begin):
        """
        Sets the time_maintenance_begin of this AutonomousDatabaseSummary.
        The date and time when maintenance will begin.


        :param time_maintenance_begin: The time_maintenance_begin of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_maintenance_begin = time_maintenance_begin

    @property
    def time_maintenance_end(self):
        """
        Gets the time_maintenance_end of this AutonomousDatabaseSummary.
        The date and time when maintenance will end.


        :return: The time_maintenance_end of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_maintenance_end

    @time_maintenance_end.setter
    def time_maintenance_end(self, time_maintenance_end):
        """
        Sets the time_maintenance_end of this AutonomousDatabaseSummary.
        The date and time when maintenance will end.


        :param time_maintenance_end: The time_maintenance_end of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_maintenance_end = time_maintenance_end

    @property
    def is_refreshable_clone(self):
        """
        Gets the is_refreshable_clone of this AutonomousDatabaseSummary.
        Indicates whether the Autonomous Database is a refreshable clone.


        :return: The is_refreshable_clone of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_refreshable_clone

    @is_refreshable_clone.setter
    def is_refreshable_clone(self, is_refreshable_clone):
        """
        Sets the is_refreshable_clone of this AutonomousDatabaseSummary.
        Indicates whether the Autonomous Database is a refreshable clone.


        :param is_refreshable_clone: The is_refreshable_clone of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_refreshable_clone = is_refreshable_clone

    @property
    def time_of_last_refresh(self):
        """
        Gets the time_of_last_refresh of this AutonomousDatabaseSummary.
        The date and time when last refresh happened.


        :return: The time_of_last_refresh of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_of_last_refresh

    @time_of_last_refresh.setter
    def time_of_last_refresh(self, time_of_last_refresh):
        """
        Sets the time_of_last_refresh of this AutonomousDatabaseSummary.
        The date and time when last refresh happened.


        :param time_of_last_refresh: The time_of_last_refresh of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_of_last_refresh = time_of_last_refresh

    @property
    def time_of_last_refresh_point(self):
        """
        Gets the time_of_last_refresh_point of this AutonomousDatabaseSummary.
        The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the refresh point is not included in the refresh.


        :return: The time_of_last_refresh_point of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_of_last_refresh_point

    @time_of_last_refresh_point.setter
    def time_of_last_refresh_point(self, time_of_last_refresh_point):
        """
        Sets the time_of_last_refresh_point of this AutonomousDatabaseSummary.
        The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the refresh point is not included in the refresh.


        :param time_of_last_refresh_point: The time_of_last_refresh_point of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_of_last_refresh_point = time_of_last_refresh_point

    @property
    def time_of_next_refresh(self):
        """
        Gets the time_of_next_refresh of this AutonomousDatabaseSummary.
        The date and time of next refresh.


        :return: The time_of_next_refresh of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_of_next_refresh

    @time_of_next_refresh.setter
    def time_of_next_refresh(self, time_of_next_refresh):
        """
        Sets the time_of_next_refresh of this AutonomousDatabaseSummary.
        The date and time of next refresh.


        :param time_of_next_refresh: The time_of_next_refresh of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_of_next_refresh = time_of_next_refresh

    @property
    def open_mode(self):
        """
        Gets the open_mode of this AutonomousDatabaseSummary.
        The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.

        Allowed values for this property are: "READ_ONLY", "READ_WRITE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The open_mode of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._open_mode

    @open_mode.setter
    def open_mode(self, open_mode):
        """
        Sets the open_mode of this AutonomousDatabaseSummary.
        The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.


        :param open_mode: The open_mode of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["READ_ONLY", "READ_WRITE"]
        if not value_allowed_none_or_none_sentinel(open_mode, allowed_values):
            open_mode = 'UNKNOWN_ENUM_VALUE'
        self._open_mode = open_mode

    @property
    def refreshable_status(self):
        """
        Gets the refreshable_status of this AutonomousDatabaseSummary.
        The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous Database.

        Allowed values for this property are: "REFRESHING", "NOT_REFRESHING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The refreshable_status of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._refreshable_status

    @refreshable_status.setter
    def refreshable_status(self, refreshable_status):
        """
        Sets the refreshable_status of this AutonomousDatabaseSummary.
        The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous Database.


        :param refreshable_status: The refreshable_status of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["REFRESHING", "NOT_REFRESHING"]
        if not value_allowed_none_or_none_sentinel(refreshable_status, allowed_values):
            refreshable_status = 'UNKNOWN_ENUM_VALUE'
        self._refreshable_status = refreshable_status

    @property
    def refreshable_mode(self):
        """
        Gets the refreshable_mode of this AutonomousDatabaseSummary.
        The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.

        Allowed values for this property are: "AUTOMATIC", "MANUAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The refreshable_mode of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._refreshable_mode

    @refreshable_mode.setter
    def refreshable_mode(self, refreshable_mode):
        """
        Sets the refreshable_mode of this AutonomousDatabaseSummary.
        The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.


        :param refreshable_mode: The refreshable_mode of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["AUTOMATIC", "MANUAL"]
        if not value_allowed_none_or_none_sentinel(refreshable_mode, allowed_values):
            refreshable_mode = 'UNKNOWN_ENUM_VALUE'
        self._refreshable_mode = refreshable_mode

    @property
    def source_id(self):
        """
        Gets the source_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the source Autonomous Database that was cloned to create the current Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the source Autonomous Database that was cloned to create the current Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._source_id = source_id

    @property
    def permission_level(self):
        """
        Gets the permission_level of this AutonomousDatabaseSummary.
        The Autonomous Database permission level. Restricted mode allows access only to admin users.

        Allowed values for this property are: "RESTRICTED", "UNRESTRICTED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The permission_level of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._permission_level

    @permission_level.setter
    def permission_level(self, permission_level):
        """
        Sets the permission_level of this AutonomousDatabaseSummary.
        The Autonomous Database permission level. Restricted mode allows access only to admin users.


        :param permission_level: The permission_level of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["RESTRICTED", "UNRESTRICTED"]
        if not value_allowed_none_or_none_sentinel(permission_level, allowed_values):
            permission_level = 'UNKNOWN_ENUM_VALUE'
        self._permission_level = permission_level

    @property
    def time_of_last_switchover(self):
        """
        Gets the time_of_last_switchover of this AutonomousDatabaseSummary.
        The timestamp of the last switchover operation for the Autonomous Database.


        :return: The time_of_last_switchover of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_of_last_switchover

    @time_of_last_switchover.setter
    def time_of_last_switchover(self, time_of_last_switchover):
        """
        Sets the time_of_last_switchover of this AutonomousDatabaseSummary.
        The timestamp of the last switchover operation for the Autonomous Database.


        :param time_of_last_switchover: The time_of_last_switchover of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_of_last_switchover = time_of_last_switchover

    @property
    def time_of_last_failover(self):
        """
        Gets the time_of_last_failover of this AutonomousDatabaseSummary.
        The timestamp of the last failover operation.


        :return: The time_of_last_failover of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_of_last_failover

    @time_of_last_failover.setter
    def time_of_last_failover(self, time_of_last_failover):
        """
        Sets the time_of_last_failover of this AutonomousDatabaseSummary.
        The timestamp of the last failover operation.


        :param time_of_last_failover: The time_of_last_failover of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_of_last_failover = time_of_last_failover

    @property
    def is_data_guard_enabled(self):
        """
        Gets the is_data_guard_enabled of this AutonomousDatabaseSummary.
        Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to
        Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.


        :return: The is_data_guard_enabled of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_data_guard_enabled

    @is_data_guard_enabled.setter
    def is_data_guard_enabled(self, is_data_guard_enabled):
        """
        Sets the is_data_guard_enabled of this AutonomousDatabaseSummary.
        Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard associations, or to
        Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.


        :param is_data_guard_enabled: The is_data_guard_enabled of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_data_guard_enabled = is_data_guard_enabled

    @property
    def failed_data_recovery_in_seconds(self):
        """
        Gets the failed_data_recovery_in_seconds of this AutonomousDatabaseSummary.
        Indicates the number of seconds of data loss for a Data Guard failover.


        :return: The failed_data_recovery_in_seconds of this AutonomousDatabaseSummary.
        :rtype: int
        """
        return self._failed_data_recovery_in_seconds

    @failed_data_recovery_in_seconds.setter
    def failed_data_recovery_in_seconds(self, failed_data_recovery_in_seconds):
        """
        Sets the failed_data_recovery_in_seconds of this AutonomousDatabaseSummary.
        Indicates the number of seconds of data loss for a Data Guard failover.


        :param failed_data_recovery_in_seconds: The failed_data_recovery_in_seconds of this AutonomousDatabaseSummary.
        :type: int
        """
        self._failed_data_recovery_in_seconds = failed_data_recovery_in_seconds

    @property
    def standby_db(self):
        """
        Gets the standby_db of this AutonomousDatabaseSummary.

        :return: The standby_db of this AutonomousDatabaseSummary.
        :rtype: oci.database.models.AutonomousDatabaseStandbySummary
        """
        return self._standby_db

    @standby_db.setter
    def standby_db(self, standby_db):
        """
        Sets the standby_db of this AutonomousDatabaseSummary.

        :param standby_db: The standby_db of this AutonomousDatabaseSummary.
        :type: oci.database.models.AutonomousDatabaseStandbySummary
        """
        self._standby_db = standby_db

    @property
    def role(self):
        """
        Gets the role of this AutonomousDatabaseSummary.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.

        Allowed values for this property are: "PRIMARY", "STANDBY", "DISABLED_STANDBY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The role of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """
        Sets the role of this AutonomousDatabaseSummary.
        The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.


        :param role: The role of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["PRIMARY", "STANDBY", "DISABLED_STANDBY"]
        if not value_allowed_none_or_none_sentinel(role, allowed_values):
            role = 'UNKNOWN_ENUM_VALUE'
        self._role = role

    @property
    def available_upgrade_versions(self):
        """
        Gets the available_upgrade_versions of this AutonomousDatabaseSummary.
        List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.


        :return: The available_upgrade_versions of this AutonomousDatabaseSummary.
        :rtype: list[str]
        """
        return self._available_upgrade_versions

    @available_upgrade_versions.setter
    def available_upgrade_versions(self, available_upgrade_versions):
        """
        Sets the available_upgrade_versions of this AutonomousDatabaseSummary.
        List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.


        :param available_upgrade_versions: The available_upgrade_versions of this AutonomousDatabaseSummary.
        :type: list[str]
        """
        self._available_upgrade_versions = available_upgrade_versions

    @property
    def key_store_id(self):
        """
        Gets the key_store_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The key_store_id of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._key_store_id

    @key_store_id.setter
    def key_store_id(self, key_store_id):
        """
        Sets the key_store_id of this AutonomousDatabaseSummary.
        The `OCID`__ of the key store.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param key_store_id: The key_store_id of this AutonomousDatabaseSummary.
        :type: str
        """
        self._key_store_id = key_store_id

    @property
    def key_store_wallet_name(self):
        """
        Gets the key_store_wallet_name of this AutonomousDatabaseSummary.
        The wallet name for Oracle Key Vault.


        :return: The key_store_wallet_name of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._key_store_wallet_name

    @key_store_wallet_name.setter
    def key_store_wallet_name(self, key_store_wallet_name):
        """
        Sets the key_store_wallet_name of this AutonomousDatabaseSummary.
        The wallet name for Oracle Key Vault.


        :param key_store_wallet_name: The key_store_wallet_name of this AutonomousDatabaseSummary.
        :type: str
        """
        self._key_store_wallet_name = key_store_wallet_name

    @property
    def supported_regions_to_clone_to(self):
        """
        Gets the supported_regions_to_clone_to of this AutonomousDatabaseSummary.
        The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.


        :return: The supported_regions_to_clone_to of this AutonomousDatabaseSummary.
        :rtype: list[str]
        """
        return self._supported_regions_to_clone_to

    @supported_regions_to_clone_to.setter
    def supported_regions_to_clone_to(self, supported_regions_to_clone_to):
        """
        Sets the supported_regions_to_clone_to of this AutonomousDatabaseSummary.
        The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.


        :param supported_regions_to_clone_to: The supported_regions_to_clone_to of this AutonomousDatabaseSummary.
        :type: list[str]
        """
        self._supported_regions_to_clone_to = supported_regions_to_clone_to

    @property
    def customer_contacts(self):
        """
        Gets the customer_contacts of this AutonomousDatabaseSummary.
        Customer Contacts.


        :return: The customer_contacts of this AutonomousDatabaseSummary.
        :rtype: list[oci.database.models.CustomerContact]
        """
        return self._customer_contacts

    @customer_contacts.setter
    def customer_contacts(self, customer_contacts):
        """
        Sets the customer_contacts of this AutonomousDatabaseSummary.
        Customer Contacts.


        :param customer_contacts: The customer_contacts of this AutonomousDatabaseSummary.
        :type: list[oci.database.models.CustomerContact]
        """
        self._customer_contacts = customer_contacts

    @property
    def time_local_data_guard_enabled(self):
        """
        Gets the time_local_data_guard_enabled of this AutonomousDatabaseSummary.
        The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.


        :return: The time_local_data_guard_enabled of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_local_data_guard_enabled

    @time_local_data_guard_enabled.setter
    def time_local_data_guard_enabled(self, time_local_data_guard_enabled):
        """
        Sets the time_local_data_guard_enabled of this AutonomousDatabaseSummary.
        The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as the primary database.


        :param time_local_data_guard_enabled: The time_local_data_guard_enabled of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_local_data_guard_enabled = time_local_data_guard_enabled

    @property
    def dataguard_region_type(self):
        """
        Gets the dataguard_region_type of this AutonomousDatabaseSummary.
        The Autonomous Data Guard region type of the Autonomous Database. For Autonomous Databases on shared Exadata infrastructure, Data Guard associations have designated primary and standby regions, and these region types do not change when the database changes roles. The standby regions in Data Guard associations can be the same region designated as the primary region, or they can be remote regions. Certain database administrative operations may be available only in the primary region of the Data Guard association, and cannot be performed when the database using the \"primary\" role is operating in a remote Data Guard standby region.

        Allowed values for this property are: "PRIMARY_DG_REGION", "REMOTE_STANDBY_DG_REGION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The dataguard_region_type of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._dataguard_region_type

    @dataguard_region_type.setter
    def dataguard_region_type(self, dataguard_region_type):
        """
        Sets the dataguard_region_type of this AutonomousDatabaseSummary.
        The Autonomous Data Guard region type of the Autonomous Database. For Autonomous Databases on shared Exadata infrastructure, Data Guard associations have designated primary and standby regions, and these region types do not change when the database changes roles. The standby regions in Data Guard associations can be the same region designated as the primary region, or they can be remote regions. Certain database administrative operations may be available only in the primary region of the Data Guard association, and cannot be performed when the database using the \"primary\" role is operating in a remote Data Guard standby region.


        :param dataguard_region_type: The dataguard_region_type of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["PRIMARY_DG_REGION", "REMOTE_STANDBY_DG_REGION"]
        if not value_allowed_none_or_none_sentinel(dataguard_region_type, allowed_values):
            dataguard_region_type = 'UNKNOWN_ENUM_VALUE'
        self._dataguard_region_type = dataguard_region_type

    @property
    def time_data_guard_role_changed(self):
        """
        Gets the time_data_guard_role_changed of this AutonomousDatabaseSummary.
        The date and time the Autonomous Data Guard role was switched for the Autonomous Database. For databases that have standbys in both the primary Data Guard region and a remote Data Guard standby region, this is the latest timestamp of either the database using the \"primary\" role in the primary Data Guard region, or database located in the remote Data Guard standby region.


        :return: The time_data_guard_role_changed of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_data_guard_role_changed

    @time_data_guard_role_changed.setter
    def time_data_guard_role_changed(self, time_data_guard_role_changed):
        """
        Sets the time_data_guard_role_changed of this AutonomousDatabaseSummary.
        The date and time the Autonomous Data Guard role was switched for the Autonomous Database. For databases that have standbys in both the primary Data Guard region and a remote Data Guard standby region, this is the latest timestamp of either the database using the \"primary\" role in the primary Data Guard region, or database located in the remote Data Guard standby region.


        :param time_data_guard_role_changed: The time_data_guard_role_changed of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_data_guard_role_changed = time_data_guard_role_changed

    @property
    def peer_db_ids(self):
        """
        Gets the peer_db_ids of this AutonomousDatabaseSummary.
        The list of `OCIDs`__ of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for shared Exadata infrastructure, standby databases located in the same region as the source primary database do not have OCIDs.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The peer_db_ids of this AutonomousDatabaseSummary.
        :rtype: list[str]
        """
        return self._peer_db_ids

    @peer_db_ids.setter
    def peer_db_ids(self, peer_db_ids):
        """
        Sets the peer_db_ids of this AutonomousDatabaseSummary.
        The list of `OCIDs`__ of standby databases located in Autonomous Data Guard remote regions that are associated with the source database. Note that for shared Exadata infrastructure, standby databases located in the same region as the source primary database do not have OCIDs.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param peer_db_ids: The peer_db_ids of this AutonomousDatabaseSummary.
        :type: list[str]
        """
        self._peer_db_ids = peer_db_ids

    @property
    def is_mtls_connection_required(self):
        """
        Gets the is_mtls_connection_required of this AutonomousDatabaseSummary.
        Indicates whether the Autonomous Database requires mTLS connections.


        :return: The is_mtls_connection_required of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_mtls_connection_required

    @is_mtls_connection_required.setter
    def is_mtls_connection_required(self, is_mtls_connection_required):
        """
        Sets the is_mtls_connection_required of this AutonomousDatabaseSummary.
        Indicates whether the Autonomous Database requires mTLS connections.


        :param is_mtls_connection_required: The is_mtls_connection_required of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_mtls_connection_required = is_mtls_connection_required

    @property
    def is_reconnect_clone_enabled(self):
        """
        Gets the is_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        Indicates if the refreshable clone can be reconnected to its source database.


        :return: The is_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        :rtype: bool
        """
        return self._is_reconnect_clone_enabled

    @is_reconnect_clone_enabled.setter
    def is_reconnect_clone_enabled(self, is_reconnect_clone_enabled):
        """
        Sets the is_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        Indicates if the refreshable clone can be reconnected to its source database.


        :param is_reconnect_clone_enabled: The is_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        :type: bool
        """
        self._is_reconnect_clone_enabled = is_reconnect_clone_enabled

    @property
    def time_until_reconnect_clone_enabled(self):
        """
        Gets the time_until_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        The time and date as an RFC3339 formatted string, e.g., 2022-01-01T12:00:00.000Z, to set the limit for a refreshable clone to be reconnected to its source database.


        :return: The time_until_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        :rtype: datetime
        """
        return self._time_until_reconnect_clone_enabled

    @time_until_reconnect_clone_enabled.setter
    def time_until_reconnect_clone_enabled(self, time_until_reconnect_clone_enabled):
        """
        Sets the time_until_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        The time and date as an RFC3339 formatted string, e.g., 2022-01-01T12:00:00.000Z, to set the limit for a refreshable clone to be reconnected to its source database.


        :param time_until_reconnect_clone_enabled: The time_until_reconnect_clone_enabled of this AutonomousDatabaseSummary.
        :type: datetime
        """
        self._time_until_reconnect_clone_enabled = time_until_reconnect_clone_enabled

    @property
    def autonomous_maintenance_schedule_type(self):
        """
        Gets the autonomous_maintenance_schedule_type of this AutonomousDatabaseSummary.
        The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database
        follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.

        Allowed values for this property are: "EARLY", "REGULAR", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The autonomous_maintenance_schedule_type of this AutonomousDatabaseSummary.
        :rtype: str
        """
        return self._autonomous_maintenance_schedule_type

    @autonomous_maintenance_schedule_type.setter
    def autonomous_maintenance_schedule_type(self, autonomous_maintenance_schedule_type):
        """
        Sets the autonomous_maintenance_schedule_type of this AutonomousDatabaseSummary.
        The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous Database
        follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the normal cycle.


        :param autonomous_maintenance_schedule_type: The autonomous_maintenance_schedule_type of this AutonomousDatabaseSummary.
        :type: str
        """
        allowed_values = ["EARLY", "REGULAR"]
        if not value_allowed_none_or_none_sentinel(autonomous_maintenance_schedule_type, allowed_values):
            autonomous_maintenance_schedule_type = 'UNKNOWN_ENUM_VALUE'
        self._autonomous_maintenance_schedule_type = autonomous_maintenance_schedule_type

    @property
    def scheduled_operations(self):
        """
        Gets the scheduled_operations of this AutonomousDatabaseSummary.
        list of scheduled operations


        :return: The scheduled_operations of this AutonomousDatabaseSummary.
        :rtype: list[oci.database.models.ScheduledOperationDetails]
        """
        return self._scheduled_operations

    @scheduled_operations.setter
    def scheduled_operations(self, scheduled_operations):
        """
        Sets the scheduled_operations of this AutonomousDatabaseSummary.
        list of scheduled operations


        :param scheduled_operations: The scheduled_operations of this AutonomousDatabaseSummary.
        :type: list[oci.database.models.ScheduledOperationDetails]
        """
        self._scheduled_operations = scheduled_operations

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
