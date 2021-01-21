# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDatabaseDetails(CreateAutonomousDatabaseBase):
    """
    Details to create an Oracle Autonomous Database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDatabaseDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateAutonomousDatabaseDetails.source` attribute
        of this class is ``NONE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousDatabaseDetails.
        :type compartment_id: str

        :param db_name:
            The value to assign to the db_name property of this CreateAutonomousDatabaseDetails.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateAutonomousDatabaseDetails.
        :type cpu_core_count: int

        :param db_workload:
            The value to assign to the db_workload property of this CreateAutonomousDatabaseDetails.
            Allowed values for this property are: "OLTP", "DW", "AJD", "APEX"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateAutonomousDatabaseDetails.
        :type data_storage_size_in_tbs: int

        :param is_free_tier:
            The value to assign to the is_free_tier property of this CreateAutonomousDatabaseDetails.
        :type is_free_tier: bool

        :param admin_password:
            The value to assign to the admin_password property of this CreateAutonomousDatabaseDetails.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDatabaseDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateAutonomousDatabaseDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_preview_version_with_service_terms_accepted:
            The value to assign to the is_preview_version_with_service_terms_accepted property of this CreateAutonomousDatabaseDetails.
        :type is_preview_version_with_service_terms_accepted: bool

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateAutonomousDatabaseDetails.
        :type is_auto_scaling_enabled: bool

        :param is_dedicated:
            The value to assign to the is_dedicated property of this CreateAutonomousDatabaseDetails.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this CreateAutonomousDatabaseDetails.
        :type autonomous_container_database_id: str

        :param is_access_control_enabled:
            The value to assign to the is_access_control_enabled property of this CreateAutonomousDatabaseDetails.
        :type is_access_control_enabled: bool

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this CreateAutonomousDatabaseDetails.
        :type whitelisted_ips: list[str]

        :param are_primary_whitelisted_ips_used:
            The value to assign to the are_primary_whitelisted_ips_used property of this CreateAutonomousDatabaseDetails.
        :type are_primary_whitelisted_ips_used: bool

        :param standby_whitelisted_ips:
            The value to assign to the standby_whitelisted_ips property of this CreateAutonomousDatabaseDetails.
        :type standby_whitelisted_ips: list[str]

        :param is_data_guard_enabled:
            The value to assign to the is_data_guard_enabled property of this CreateAutonomousDatabaseDetails.
        :type is_data_guard_enabled: bool

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateAutonomousDatabaseDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateAutonomousDatabaseDetails.
        :type nsg_ids: list[str]

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this CreateAutonomousDatabaseDetails.
        :type private_endpoint_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param db_version:
            The value to assign to the db_version property of this CreateAutonomousDatabaseDetails.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateAutonomousDatabaseDetails.
            Allowed values for this property are: "NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP", "CLONE_TO_REFRESHABLE"
        :type source: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'db_workload': 'str',
            'data_storage_size_in_tbs': 'int',
            'is_free_tier': 'bool',
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
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'private_endpoint_label': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'db_version': 'str',
            'source': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'db_workload': 'dbWorkload',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'is_free_tier': 'isFreeTier',
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
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'private_endpoint_label': 'privateEndpointLabel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'db_version': 'dbVersion',
            'source': 'source'
        }

        self._compartment_id = None
        self._db_name = None
        self._cpu_core_count = None
        self._db_workload = None
        self._data_storage_size_in_tbs = None
        self._is_free_tier = None
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
        self._subnet_id = None
        self._nsg_ids = None
        self._private_endpoint_label = None
        self._freeform_tags = None
        self._defined_tags = None
        self._db_version = None
        self._source = None
        self._source = 'NONE'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
