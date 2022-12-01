# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateVolumeMountDetails(object):
    """
    Define the mapping from volume to a mount path in container.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateVolumeMountDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mount_path:
            The value to assign to the mount_path property of this CreateVolumeMountDetails.
        :type mount_path: str

        :param volume_name:
            The value to assign to the volume_name property of this CreateVolumeMountDetails.
        :type volume_name: str

        :param sub_path:
            The value to assign to the sub_path property of this CreateVolumeMountDetails.
        :type sub_path: str

        :param is_read_only:
            The value to assign to the is_read_only property of this CreateVolumeMountDetails.
        :type is_read_only: bool

        :param partition:
            The value to assign to the partition property of this CreateVolumeMountDetails.
        :type partition: int

        """
        self.swagger_types = {
            'mount_path': 'str',
            'volume_name': 'str',
            'sub_path': 'str',
            'is_read_only': 'bool',
            'partition': 'int'
        }

        self.attribute_map = {
            'mount_path': 'mountPath',
            'volume_name': 'volumeName',
            'sub_path': 'subPath',
            'is_read_only': 'isReadOnly',
            'partition': 'partition'
        }

        self._mount_path = None
        self._volume_name = None
        self._sub_path = None
        self._is_read_only = None
        self._partition = None

    @property
    def mount_path(self):
        """
        **[Required]** Gets the mount_path of this CreateVolumeMountDetails.
        mountPath describes the volume access path.


        :return: The mount_path of this CreateVolumeMountDetails.
        :rtype: str
        """
        return self._mount_path

    @mount_path.setter
    def mount_path(self, mount_path):
        """
        Sets the mount_path of this CreateVolumeMountDetails.
        mountPath describes the volume access path.


        :param mount_path: The mount_path of this CreateVolumeMountDetails.
        :type: str
        """
        self._mount_path = mount_path

    @property
    def volume_name(self):
        """
        **[Required]** Gets the volume_name of this CreateVolumeMountDetails.
        The name of the volume.


        :return: The volume_name of this CreateVolumeMountDetails.
        :rtype: str
        """
        return self._volume_name

    @volume_name.setter
    def volume_name(self, volume_name):
        """
        Sets the volume_name of this CreateVolumeMountDetails.
        The name of the volume.


        :param volume_name: The volume_name of this CreateVolumeMountDetails.
        :type: str
        """
        self._volume_name = volume_name

    @property
    def sub_path(self):
        """
        Gets the sub_path of this CreateVolumeMountDetails.
        specifies a sub-path inside the referenced volume instead of its root


        :return: The sub_path of this CreateVolumeMountDetails.
        :rtype: str
        """
        return self._sub_path

    @sub_path.setter
    def sub_path(self, sub_path):
        """
        Sets the sub_path of this CreateVolumeMountDetails.
        specifies a sub-path inside the referenced volume instead of its root


        :param sub_path: The sub_path of this CreateVolumeMountDetails.
        :type: str
        """
        self._sub_path = sub_path

    @property
    def is_read_only(self):
        """
        Gets the is_read_only of this CreateVolumeMountDetails.
        Whether the volume was mounted in read-only mode. Defaults to false if not specified.


        :return: The is_read_only of this CreateVolumeMountDetails.
        :rtype: bool
        """
        return self._is_read_only

    @is_read_only.setter
    def is_read_only(self, is_read_only):
        """
        Sets the is_read_only of this CreateVolumeMountDetails.
        Whether the volume was mounted in read-only mode. Defaults to false if not specified.


        :param is_read_only: The is_read_only of this CreateVolumeMountDetails.
        :type: bool
        """
        self._is_read_only = is_read_only

    @property
    def partition(self):
        """
        Gets the partition of this CreateVolumeMountDetails.
        If there is more than 1 partitions in the volume, this is the number of partition which be referenced.
        Here is a example:
        Number  Start   End     Size    File system  Name                  Flags
         1      1049kB  106MB   105MB   fat16        EFI System Partition  boot, esp
         2      106MB   1180MB  1074MB  xfs
         3      1180MB  50.0GB  48.8GB                                     lvm


        :return: The partition of this CreateVolumeMountDetails.
        :rtype: int
        """
        return self._partition

    @partition.setter
    def partition(self, partition):
        """
        Sets the partition of this CreateVolumeMountDetails.
        If there is more than 1 partitions in the volume, this is the number of partition which be referenced.
        Here is a example:
        Number  Start   End     Size    File system  Name                  Flags
         1      1049kB  106MB   105MB   fat16        EFI System Partition  boot, esp
         2      106MB   1180MB  1074MB  xfs
         3      1180MB  50.0GB  48.8GB                                     lvm


        :param partition: The partition of this CreateVolumeMountDetails.
        :type: int
        """
        self._partition = partition

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
