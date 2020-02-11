# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from .create_autonomous_database_base import CreateAutonomousDatabaseBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAutonomousDatabaseCloneDetails(CreateAutonomousDatabaseBase):
    """
    Details to create an Oracle Autonomous Database by cloning an existing Autonomous Database.
    """

    #: A constant which can be used with the clone_type property of a CreateAutonomousDatabaseCloneDetails.
    #: This constant has a value of "FULL"
    CLONE_TYPE_FULL = "FULL"

    #: A constant which can be used with the clone_type property of a CreateAutonomousDatabaseCloneDetails.
    #: This constant has a value of "METADATA"
    CLONE_TYPE_METADATA = "METADATA"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAutonomousDatabaseCloneDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateAutonomousDatabaseCloneDetails.source` attribute
        of this class is ``DATABASE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAutonomousDatabaseCloneDetails.
        :type compartment_id: str

        :param db_name:
            The value to assign to the db_name property of this CreateAutonomousDatabaseCloneDetails.
        :type db_name: str

        :param cpu_core_count:
            The value to assign to the cpu_core_count property of this CreateAutonomousDatabaseCloneDetails.
        :type cpu_core_count: int

        :param db_workload:
            The value to assign to the db_workload property of this CreateAutonomousDatabaseCloneDetails.
            Allowed values for this property are: "OLTP", "DW"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateAutonomousDatabaseCloneDetails.
        :type data_storage_size_in_tbs: int

        :param is_free_tier:
            The value to assign to the is_free_tier property of this CreateAutonomousDatabaseCloneDetails.
        :type is_free_tier: bool

        :param admin_password:
            The value to assign to the admin_password property of this CreateAutonomousDatabaseCloneDetails.
        :type admin_password: str

        :param display_name:
            The value to assign to the display_name property of this CreateAutonomousDatabaseCloneDetails.
        :type display_name: str

        :param license_model:
            The value to assign to the license_model property of this CreateAutonomousDatabaseCloneDetails.
            Allowed values for this property are: "LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"
        :type license_model: str

        :param is_preview_version_with_service_terms_accepted:
            The value to assign to the is_preview_version_with_service_terms_accepted property of this CreateAutonomousDatabaseCloneDetails.
        :type is_preview_version_with_service_terms_accepted: bool

        :param is_auto_scaling_enabled:
            The value to assign to the is_auto_scaling_enabled property of this CreateAutonomousDatabaseCloneDetails.
        :type is_auto_scaling_enabled: bool

        :param is_dedicated:
            The value to assign to the is_dedicated property of this CreateAutonomousDatabaseCloneDetails.
        :type is_dedicated: bool

        :param autonomous_container_database_id:
            The value to assign to the autonomous_container_database_id property of this CreateAutonomousDatabaseCloneDetails.
        :type autonomous_container_database_id: str

        :param whitelisted_ips:
            The value to assign to the whitelisted_ips property of this CreateAutonomousDatabaseCloneDetails.
        :type whitelisted_ips: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDatabaseCloneDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDatabaseCloneDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param db_version:
            The value to assign to the db_version property of this CreateAutonomousDatabaseCloneDetails.
        :type db_version: str

        :param source:
            The value to assign to the source property of this CreateAutonomousDatabaseCloneDetails.
            Allowed values for this property are: "NONE", "DATABASE", "BACKUP_FROM_ID", "BACKUP_FROM_TIMESTAMP"
        :type source: str

        :param source_id:
            The value to assign to the source_id property of this CreateAutonomousDatabaseCloneDetails.
        :type source_id: str

        :param clone_type:
            The value to assign to the clone_type property of this CreateAutonomousDatabaseCloneDetails.
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
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'db_version': 'str',
            'source': 'str',
            'source_id': 'str',
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
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'db_version': 'dbVersion',
            'source': 'source',
            'source_id': 'sourceId',
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
        self._freeform_tags = None
        self._defined_tags = None
        self._db_version = None
        self._source = None
        self._source_id = None
        self._clone_type = None
        self._source = 'DATABASE'

    @property
    def source_id(self):
        """
        **[Required]** Gets the source_id of this CreateAutonomousDatabaseCloneDetails.
        The `OCID`__ of the source Autonomous Database that you will clone to create a new Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The source_id of this CreateAutonomousDatabaseCloneDetails.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        """
        Sets the source_id of this CreateAutonomousDatabaseCloneDetails.
        The `OCID`__ of the source Autonomous Database that you will clone to create a new Autonomous Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param source_id: The source_id of this CreateAutonomousDatabaseCloneDetails.
        :type: str
        """
        self._source_id = source_id

    @property
    def clone_type(self):
        """
        **[Required]** Gets the clone_type of this CreateAutonomousDatabaseCloneDetails.
        The Autonomous Database clone type.

        Allowed values for this property are: "FULL", "METADATA"


        :return: The clone_type of this CreateAutonomousDatabaseCloneDetails.
        :rtype: str
        """
        return self._clone_type

    @clone_type.setter
    def clone_type(self, clone_type):
        """
        Sets the clone_type of this CreateAutonomousDatabaseCloneDetails.
        The Autonomous Database clone type.


        :param clone_type: The clone_type of this CreateAutonomousDatabaseCloneDetails.
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
