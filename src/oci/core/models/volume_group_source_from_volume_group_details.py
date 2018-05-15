# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .volume_group_source_details import VolumeGroupSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroupSourceFromVolumeGroupDetails(VolumeGroupSourceDetails):
    """
    Specifies the volume group to clone from.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroupSourceFromVolumeGroupDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VolumeGroupSourceFromVolumeGroupDetails.type` attribute
        of this class is ``volumeGroupId`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VolumeGroupSourceFromVolumeGroupDetails.
        :type type: str

        :param volume_group_id:
            The value to assign to the volume_group_id property of this VolumeGroupSourceFromVolumeGroupDetails.
        :type volume_group_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'volume_group_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'volume_group_id': 'volumeGroupId'
        }

        self._type = None
        self._volume_group_id = None
        self._type = 'volumeGroupId'

    @property
    def volume_group_id(self):
        """
        **[Required]** Gets the volume_group_id of this VolumeGroupSourceFromVolumeGroupDetails.
        The OCID of the volume group to clone from.


        :return: The volume_group_id of this VolumeGroupSourceFromVolumeGroupDetails.
        :rtype: str
        """
        return self._volume_group_id

    @volume_group_id.setter
    def volume_group_id(self, volume_group_id):
        """
        Sets the volume_group_id of this VolumeGroupSourceFromVolumeGroupDetails.
        The OCID of the volume group to clone from.


        :param volume_group_id: The volume_group_id of this VolumeGroupSourceFromVolumeGroupDetails.
        :type: str
        """
        self._volume_group_id = volume_group_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
