# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .volume_group_source_details import VolumeGroupSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeGroupSourceFromVolumesDetails(VolumeGroupSourceDetails):
    """
    Specifies volumes in a volume group.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeGroupSourceFromVolumesDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.VolumeGroupSourceFromVolumesDetails.type` attribute
        of this class is ``volumeIds`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VolumeGroupSourceFromVolumesDetails.
        :type type: str

        :param volume_ids:
            The value to assign to the volume_ids property of this VolumeGroupSourceFromVolumesDetails.
        :type volume_ids: list[str]

        """
        self.swagger_types = {
            'type': 'str',
            'volume_ids': 'list[str]'
        }

        self.attribute_map = {
            'type': 'type',
            'volume_ids': 'volumeIds'
        }

        self._type = None
        self._volume_ids = None
        self._type = 'volumeIds'

    @property
    def volume_ids(self):
        """
        **[Required]** Gets the volume_ids of this VolumeGroupSourceFromVolumesDetails.
        OCIDs for the volumes in this volume group.


        :return: The volume_ids of this VolumeGroupSourceFromVolumesDetails.
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """
        Sets the volume_ids of this VolumeGroupSourceFromVolumesDetails.
        OCIDs for the volumes in this volume group.


        :param volume_ids: The volume_ids of this VolumeGroupSourceFromVolumesDetails.
        :type: list[str]
        """
        self._volume_ids = volume_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
