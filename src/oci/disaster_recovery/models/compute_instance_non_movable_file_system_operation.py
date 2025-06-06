# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ComputeInstanceNonMovableFileSystemOperation(object):
    """
    The details of operations performed on a file system.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ComputeInstanceNonMovableFileSystemOperation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param export_path:
            The value to assign to the export_path property of this ComputeInstanceNonMovableFileSystemOperation.
        :type export_path: str

        :param mount_point:
            The value to assign to the mount_point property of this ComputeInstanceNonMovableFileSystemOperation.
        :type mount_point: str

        :param mount_target_id:
            The value to assign to the mount_target_id property of this ComputeInstanceNonMovableFileSystemOperation.
        :type mount_target_id: str

        """
        self.swagger_types = {
            'export_path': 'str',
            'mount_point': 'str',
            'mount_target_id': 'str'
        }
        self.attribute_map = {
            'export_path': 'exportPath',
            'mount_point': 'mountPoint',
            'mount_target_id': 'mountTargetId'
        }
        self._export_path = None
        self._mount_point = None
        self._mount_target_id = None

    @property
    def export_path(self):
        """
        **[Required]** Gets the export_path of this ComputeInstanceNonMovableFileSystemOperation.
        The export path of the file system.

        Example: `/fs-export-path`


        :return: The export_path of this ComputeInstanceNonMovableFileSystemOperation.
        :rtype: str
        """
        return self._export_path

    @export_path.setter
    def export_path(self, export_path):
        """
        Sets the export_path of this ComputeInstanceNonMovableFileSystemOperation.
        The export path of the file system.

        Example: `/fs-export-path`


        :param export_path: The export_path of this ComputeInstanceNonMovableFileSystemOperation.
        :type: str
        """
        self._export_path = export_path

    @property
    def mount_point(self):
        """
        **[Required]** Gets the mount_point of this ComputeInstanceNonMovableFileSystemOperation.
        The physical mount point of the file system on a host.

        Example: `/mnt/yourmountpoint`


        :return: The mount_point of this ComputeInstanceNonMovableFileSystemOperation.
        :rtype: str
        """
        return self._mount_point

    @mount_point.setter
    def mount_point(self, mount_point):
        """
        Sets the mount_point of this ComputeInstanceNonMovableFileSystemOperation.
        The physical mount point of the file system on a host.

        Example: `/mnt/yourmountpoint`


        :param mount_point: The mount_point of this ComputeInstanceNonMovableFileSystemOperation.
        :type: str
        """
        self._mount_point = mount_point

    @property
    def mount_target_id(self):
        """
        **[Required]** Gets the mount_target_id of this ComputeInstanceNonMovableFileSystemOperation.
        The OCID of mount target.

        Example: `ocid1.mounttarget.oc1..uniqueID`


        :return: The mount_target_id of this ComputeInstanceNonMovableFileSystemOperation.
        :rtype: str
        """
        return self._mount_target_id

    @mount_target_id.setter
    def mount_target_id(self, mount_target_id):
        """
        Sets the mount_target_id of this ComputeInstanceNonMovableFileSystemOperation.
        The OCID of mount target.

        Example: `ocid1.mounttarget.oc1..uniqueID`


        :param mount_target_id: The mount_target_id of this ComputeInstanceNonMovableFileSystemOperation.
        :type: str
        """
        self._mount_target_id = mount_target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
