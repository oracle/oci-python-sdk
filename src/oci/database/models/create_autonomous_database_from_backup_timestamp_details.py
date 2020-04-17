# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDatabaseFromBackupTimestampDetails(CreateAutonomousDatabaseBase):
    """
    Details to create a point-in-time clone of an Oracle Autonomous Database by specifying a timestamp. Point-in-time clones use backups as the source of the data for the clone.
    """

    #: A constant which can be used with the clone_type property of a CreateAutonomousDatabaseFromBackupTimestampDetails.
    #: This constant has a value of "FULL"
    CLONE_TYPE_FULL = "FULL"

    #: A constant which can be used with the clone_type property of a CreateAutonomousDatabaseFromBackupTimestampDetails.
    #: This constant has a value of "METADATA"
    CLONE_TYPE_METADATA = "METADATA"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDatabaseFromBackupTimestampDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateAutonomousDatabaseFromBackupTimestampDetails.source` attribute
        of this class is ``BACKUP_FROM_TIMESTAMP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type compartment_id: str

        :param db_name:
            The value to assign to the db_name property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type cpu_core_count: int

        :param db_workload:
            The value to assign to the db_workload property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
            Allowed values for this property are: "OLTP", "DW"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type data_storage_size_in_tbs: int

        :param is_free_tier:
            The value to assign to the is_free_tier property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type is_free_tier: bool

        :param admin_password:
            The value to assign to the admin_password property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_preview_version_with_service_terms_accepted:
            The value to assign to the is_preview_version_with_service_terms_accepted property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type is_preview_version_with_service_terms_accepted: bool

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type is_auto_scaling_enabled: bool

        :param is_dedicated:
            The value to assign to the is_dedicated property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type autonomous_container_database_id: str

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type whitelisted_ips: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type nsg_ids: list[str]

        :param private_endpoint_label:
            The value to assign to the private_endpoint_label property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type private_endpoint_label: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param db_version:
            The value to assign to the db_version property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
            Allowed values for this property are: "NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP"
        :type source: str

        :param autonomous_database_id:
            The value to assign to the autonomous_database_id property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type autonomous_database_id: str

        :param timestamp:
            The value to assign to the timestamp property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type timestamp: datetime

        :param clone_type:
            The value to assign to the clone_type property of this CreateAutonomousDatabaseFromBackupTimestampDetails.
            Allowed values for this property are: "FULL", "METADATA"
        :type clone_type: str

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
            'whitelisted_ips': 'list[str]',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'private_endpoint_label': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'db_version': 'str',
            'source': 'str',
            'autonomous_database_id': 'str',
            'timestamp': 'datetime',
            'clone_type': 'str'
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
            'whitelisted_ips': 'whitelistedIps',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'private_endpoint_label': 'privateEndpointLabel',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'db_version': 'dbVersion',
            'source': 'source',
            'autonomous_database_id': 'autonomousDatabaseId',
            'timestamp': 'timestamp',
            'clone_type': 'cloneType'
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
        self._whitelisted_ips = None
        self._subnet_id = None
        self._nsg_ids = None
        self._private_endpoint_label = None
        self._freeform_tags = None
        self._defined_tags = None
        self._db_version = None
        self._source = None
        self._autonomous_database_id = None
        self._timestamp = None
        self._clone_type = None
        self._source = 'BACKUP_FROM_TIMESTAMP'

    @property
    def autonomous_database_id(self):
        """
        **[Required]** Gets the autonomous_database_id of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        The `OCID`__ of the source Autonomous Database that you will clone to create a new Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The autonomous_database_id of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :rtype: str
        """
        return self._autonomous_database_id

    @autonomous_database_id.setter
    def autonomous_database_id(self, autonomous_database_id):
        """
        Sets the autonomous_database_id of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        The `OCID`__ of the source Autonomous Database that you will clone to create a new Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param autonomous_database_id: The autonomous_database_id of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type: str
        """
        self._autonomous_database_id = autonomous_database_id

    @property
    def timestamp(self):
        """
        **[Required]** Gets the timestamp of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        The timestamp specified for the point-in-time clone of the source Autonomous Database. The timestamp must be in the past.


        :return: The timestamp of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        The timestamp specified for the point-in-time clone of the source Autonomous Database. The timestamp must be in the past.


        :param timestamp: The timestamp of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type: datetime
        """
        self._timestamp = timestamp

    @property
    def clone_type(self):
        """
        **[Required]** Gets the clone_type of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        The Autonomous Database clone type.

        Allowed values for this property are: "FULL", "METADATA"


        :return: The clone_type of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :rtype: str
        """
        return self._clone_type

    @clone_type.setter
    def clone_type(self, clone_type):
        """
        Sets the clone_type of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        The Autonomous Database clone type.


        :param clone_type: The clone_type of this CreateAutonomousDatabaseFromBackupTimestampDetails.
        :type: str
        """
        allowed_values = ["FULL", "METADATA"]
        if not value_allowed_none_or_none_sentinel(clone_type, allowed_values):
            raise ValueError(
                "Invalid value for `clone_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._clone_type = clone_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
