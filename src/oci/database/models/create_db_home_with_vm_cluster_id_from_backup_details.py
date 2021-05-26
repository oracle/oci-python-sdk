# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_db_home_base import CreateDbHomeBase
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDbHomeWithVmClusterIdFromBackupDetails(CreateDbHomeBase):
    """
    Note that a valid `vmClusterId` value must be supplied for the `CreateDbHomeWithVmClusterIdFromBackup` API operation to successfully complete.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDbHomeWithVmClusterIdFromBackupDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateDbHomeWithVmClusterIdFromBackupDetails.source` attribute
        of this class is ``VM_CLUSTER_BACKUP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type display_name: str

        :param kms_key_id:
            The value to assign to the kms_key_id property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type kms_key_id: str

        :param kms_key_version_id:
            The value to assign to the kms_key_version_id property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type kms_key_version_id: str

        :param database_software_image_id:
            The value to assign to the database_software_image_id property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type database_software_image_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param source:
            The value to assign to the source property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP", "DATABASE", "VM_CLUSTER_BACKUP", "VM_CLUSTER_NEW"
        :type source: str

        :param is_desupported_version:
            The value to assign to the is_desupported_version property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type is_desupported_version: bool

        :param vm_cluster_id:
            The value to assign to the vm_cluster_id property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type vm_cluster_id: str

        :param database:
            The value to assign to the database property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type database: oci.database.models.CreateDatabaseFromBackupDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'kms_key_id': 'str',
            'kms_key_version_id': 'str',
            'database_software_image_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'source': 'str',
            'is_desupported_version': 'bool',
            'vm_cluster_id': 'str',
            'database': 'CreateDatabaseFromBackupDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'kms_key_id': 'kmsKeyId',
            'kms_key_version_id': 'kmsKeyVersionId',
            'database_software_image_id': 'databaseSoftwareImageId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'source': 'source',
            'is_desupported_version': 'isDesupportedVersion',
            'vm_cluster_id': 'vmClusterId',
            'database': 'database'
        }

        self._display_name = None
        self._kms_key_id = None
        self._kms_key_version_id = None
        self._database_software_image_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._source = None
        self._is_desupported_version = None
        self._vm_cluster_id = None
        self._database = None
        self._source = 'VM_CLUSTER_BACKUP'

    @property
    def vm_cluster_id(self):
        """
        **[Required]** Gets the vm_cluster_id of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        The `OCID`__ of the VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vm_cluster_id of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :rtype: str
        """
        return self._vm_cluster_id

    @vm_cluster_id.setter
    def vm_cluster_id(self, vm_cluster_id):
        """
        Sets the vm_cluster_id of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        The `OCID`__ of the VM cluster.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vm_cluster_id: The vm_cluster_id of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type: str
        """
        self._vm_cluster_id = vm_cluster_id

    @property
    def database(self):
        """
        **[Required]** Gets the database of this CreateDbHomeWithVmClusterIdFromBackupDetails.

        :return: The database of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :rtype: oci.database.models.CreateDatabaseFromBackupDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeWithVmClusterIdFromBackupDetails.

        :param database: The database of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type: oci.database.models.CreateDatabaseFromBackupDetails
        """
        self._database = database

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
