# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.

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

        :param source:
            The value to assign to the source property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
            Allowed values for this property are: "NONE", "DB_BACKUP", "VM_CLUSTER_NEW", "VM_CLUSTER_BACKUP"
        :type source: str

        :param vm_cluster_id:
            The value to assign to the vm_cluster_id property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type vm_cluster_id: str

        :param database:
            The value to assign to the database property of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type database: CreateDatabaseFromBackupDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'source': 'str',
            'vm_cluster_id': 'str',
            'database': 'CreateDatabaseFromBackupDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'source': 'source',
            'vm_cluster_id': 'vmClusterId',
            'database': 'database'
        }

        self._display_name = None
        self._source = None
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
        :rtype: CreateDatabaseFromBackupDetails
        """
        return self._database

    @database.setter
    def database(self, database):
        """
        Sets the database of this CreateDbHomeWithVmClusterIdFromBackupDetails.

        :param database: The database of this CreateDbHomeWithVmClusterIdFromBackupDetails.
        :type: CreateDatabaseFromBackupDetails
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
