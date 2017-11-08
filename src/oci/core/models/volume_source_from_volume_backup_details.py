# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .volume_source_details import VolumeSourceDetails
from ...util import formatted_flat_dict
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeSourceFromVolumeBackupDetails(VolumeSourceDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeSourceFromVolumeBackupDetails object with values from values from keyword arguments. The
        following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VolumeSourceFromVolumeBackupDetails.
        :type id: str

        """
        self.swagger_types = {
            'type': 'str',
            'id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'id': 'id'
        }

        self._type = None
        self._id = None
        self._type = 'volumeBackup'

    @property
    def id(self):
        """
        Gets the id of this VolumeSourceFromVolumeBackupDetails.
        The OCID of the volume backup.


        :return: The id of this VolumeSourceFromVolumeBackupDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VolumeSourceFromVolumeBackupDetails.
        The OCID of the volume backup.


        :param id: The id of this VolumeSourceFromVolumeBackupDetails.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
