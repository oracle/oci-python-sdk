# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .mount_type_details import MountTypeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SelfMountDetails(MountTypeDetails):
    """
    Used for creating NFS Self mount backup destinations for non-autonomous ExaCC.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SelfMountDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.database.models.SelfMountDetails.mount_type` attribute
        of this class is ``SELF_MOUNT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mount_type:
            The value to assign to the mount_type property of this SelfMountDetails.
            Allowed values for this property are: "SELF_MOUNT", "AUTOMATED_MOUNT"
        :type mount_type: str

        :param local_mount_point_path:
            The value to assign to the local_mount_point_path property of this SelfMountDetails.
        :type local_mount_point_path: str

        """
        self.swagger_types = {
            'mount_type': 'str',
            'local_mount_point_path': 'str'
        }

        self.attribute_map = {
            'mount_type': 'mountType',
            'local_mount_point_path': 'localMountPointPath'
        }

        self._mount_type = None
        self._local_mount_point_path = None
        self._mount_type = 'SELF_MOUNT'

    @property
    def local_mount_point_path(self):
        """
        **[Required]** Gets the local_mount_point_path of this SelfMountDetails.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :return: The local_mount_point_path of this SelfMountDetails.
        :rtype: str
        """
        return self._local_mount_point_path

    @local_mount_point_path.setter
    def local_mount_point_path(self, local_mount_point_path):
        """
        Sets the local_mount_point_path of this SelfMountDetails.
        The local directory path on each VM cluster node where the NFS server location is mounted. The local directory path and the NFS server location must each be the same across all of the VM cluster nodes. Ensure that the NFS mount is maintained continuously on all of the VM cluster nodes.


        :param local_mount_point_path: The local_mount_point_path of this SelfMountDetails.
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
