# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.

from .create_backup_destination_details import CreateBackupDestinationDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNFSBackupDestinationDetails(CreateBackupDestinationDetails):
    """
    Used for creating NFS backup destinations.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNFSBackupDestinationDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.CreateNFSBackupDestinationDetails.type` attribute
        of this class is ``NFS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateNFSBackupDestinationDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNFSBackupDestinationDetails.
        :type compartment_id: str

        :param type:
            The value to assign to the type property of this CreateNFSBackupDestinationDetails.
            Allowed values for this property are: "NFS", "RECOVERY_APPLIANCE"
        :type type: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNFSBackupDestinationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNFSBackupDestinationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param local_mount_point_path:
            The value to assign to the local_mount_point_path property of this CreateNFSBackupDestinationDetails.
        :type local_mount_point_path: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'type': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'local_mount_point_path': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'type': 'type',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'local_mount_point_path': 'localMountPointPath'
        }

        self._display_name = None
        self._compartment_id = None
        self._type = None
        self._freeform_tags = None
        self._defined_tags = None
        self._local_mount_point_path = None
        self._type = 'NFS'

    @property
    def local_mount_point_path(self):
        """
        **[Required]** Gets the local_mount_point_path of this CreateNFSBackupDestinationDetails.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :return: The local_mount_point_path of this CreateNFSBackupDestinationDetails.
        :rtype: str
        """
        return self._local_mount_point_path

    @local_mount_point_path.setter
    def local_mount_point_path(self, local_mount_point_path):
        """
        Sets the local_mount_point_path of this CreateNFSBackupDestinationDetails.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :param local_mount_point_path: The local_mount_point_path of this CreateNFSBackupDestinationDetails.
        :type: str
        """
        self._local_mount_point_path = local_mount_point_path

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
