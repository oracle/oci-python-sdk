# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class CreateVolumeBackupDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'volume_id': 'volumeId'
        }

        self._display_name = None
        self._volume_id = None

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateVolumeBackupDetails.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.


        :return: The display_name of this CreateVolumeBackupDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateVolumeBackupDetails.
        A user-friendly name for the volume backup. Does not have to be unique and it's changeable.


        :param display_name: The display_name of this CreateVolumeBackupDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def volume_id(self):
        """
        Gets the volume_id of this CreateVolumeBackupDetails.
        The OCID of the volume that needs to be backed up.


        :return: The volume_id of this CreateVolumeBackupDetails.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """
        Sets the volume_id of this CreateVolumeBackupDetails.
        The OCID of the volume that needs to be backed up.


        :param volume_id: The volume_id of this CreateVolumeBackupDetails.
        :type: str
        """
        self._volume_id = volume_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
