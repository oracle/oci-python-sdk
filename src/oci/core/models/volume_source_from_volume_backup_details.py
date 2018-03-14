# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .volume_source_details import VolumeSourceDetails
from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeSourceFromVolumeBackupDetails(VolumeSourceDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeSourceFromVolumeBackupDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VolumeSourceFromVolumeBackupDetails.type` attribute
        of this class is ``volumeBackup`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VolumeSourceFromVolumeBackupDetails.
        :type type: str

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
        **[Required]** Gets the id of this VolumeSourceFromVolumeBackupDetails.
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
