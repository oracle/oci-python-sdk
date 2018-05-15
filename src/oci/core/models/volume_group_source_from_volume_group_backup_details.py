# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .volume_group_source_details import VolumeGroupSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroupSourceFromVolumeGroupBackupDetails(VolumeGroupSourceDetails):
    """
    Specifies the volume group backup to restore from.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroupSourceFromVolumeGroupBackupDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VolumeGroupSourceFromVolumeGroupBackupDetails.type` attribute
        of this class is ``volumeGroupBackupId`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VolumeGroupSourceFromVolumeGroupBackupDetails.
        :type type: str

        :param volume_group_backup_id:
            The value to assign to the volume_group_backup_id property of this VolumeGroupSourceFromVolumeGroupBackupDetails.
        :type volume_group_backup_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'volume_group_backup_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'volume_group_backup_id': 'volumeGroupBackupId'
        }

        self._type = None
        self._volume_group_backup_id = None
        self._type = 'volumeGroupBackupId'

    @property
    def volume_group_backup_id(self):
        """
        **[Required]** Gets the volume_group_backup_id of this VolumeGroupSourceFromVolumeGroupBackupDetails.
        The OCID of the volume group backup to restore from.


        :return: The volume_group_backup_id of this VolumeGroupSourceFromVolumeGroupBackupDetails.
        :rtype: str
        """
        return self._volume_group_backup_id

    @volume_group_backup_id.setter
    def volume_group_backup_id(self, volume_group_backup_id):
        """
        Sets the volume_group_backup_id of this VolumeGroupSourceFromVolumeGroupBackupDetails.
        The OCID of the volume group backup to restore from.


        :param volume_group_backup_id: The volume_group_backup_id of this VolumeGroupSourceFromVolumeGroupBackupDetails.
        :type: str
        """
        self._volume_group_backup_id = volume_group_backup_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
