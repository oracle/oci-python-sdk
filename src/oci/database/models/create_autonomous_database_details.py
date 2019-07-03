# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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
            Allowed values for this property are: "OLTP", "DW"
        :type db_workload: str

        :param data_storage_size_in_tbs:
            The value to assign to the data_storage_size_in_tbs property of this CreateAutonomousDatabaseDetails.
        :type data_storage_size_in_tbs: int

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

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAutonomousDatabaseDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAutonomousDatabaseDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param source:
            The value to assign to the source property of this CreateAutonomousDatabaseDetails.
            Allowed values for this property are: "NONE", "DATABASE"
        :type source: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'db_name': 'str',
            'cpu_core_count': 'int',
            'db_workload': 'str',
            'data_storage_size_in_tbs': 'int',
            'admin_password': 'str',
            'display_name': 'str',
            'license_model': 'str',
            'is_preview_version_with_service_terms_accepted': 'bool',
            'is_auto_scaling_enabled': 'bool',
            'is_dedicated': 'bool',
            'autonomous_container_database_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'source': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'db_name': 'dbName',
            'cpu_core_count': 'cpuCoreCount',
            'db_workload': 'dbWorkload',
            'data_storage_size_in_tbs': 'dataStorageSizeInTBs',
            'admin_password': 'adminPassword',
            'display_name': 'displayName',
            'license_model': 'licenseModel',
            'is_preview_version_with_service_terms_accepted': 'isPreviewVersionWithServiceTermsAccepted',
            'is_auto_scaling_enabled': 'isAutoScalingEnabled',
            'is_dedicated': 'isDedicated',
            'autonomous_container_database_id': 'autonomousContainerDatabaseId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'source': 'source'
        }

        self._compartment_id = None
        self._db_name = None
        self._cpu_core_count = None
        self._db_workload = None
        self._data_storage_size_in_tbs = None
        self._admin_password = None
        self._display_name = None
        self._license_model = None
        self._is_preview_version_with_service_terms_accepted = None
        self._is_auto_scaling_enabled = None
        self._is_dedicated = None
        self._autonomous_container_database_id = None
        self._freeform_tags = None
        self._defined_tags = None
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
