# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .attach_volume_details import AttachVolumeDetails
from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachParavirtualizedVolumeDetails(AttachVolumeDetails):

    def __init__(self, **kwargs):
        """
        Initializes a new AttachParavirtualizedVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.AttachParavirtualizedVolumeDetails.type` attribute
        of this class is ``paravirtualized`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this AttachParavirtualizedVolumeDetails.
        :type display_name: str

        :param instance_id:
            The value to assign to the instance_id property of this AttachParavirtualizedVolumeDetails.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this AttachParavirtualizedVolumeDetails.
        :type is_read_only: bool

        :param type:
            The value to assign to the type property of this AttachParavirtualizedVolumeDetails.
        :type type: str

        :param volume_id:
            The value to assign to the volume_id property of this AttachParavirtualizedVolumeDetails.
        :type volume_id: str

        """
        self.swagger_types = {
            'display_name': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
            'type': 'str',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'is_read_only': 'isReadOnly',
            'type': 'type',
            'volume_id': 'volumeId'
        }

        self._display_name = None
        self._instance_id = None
        self._is_read_only = None
        self._type = None
        self._volume_id = None
        self._type = 'paravirtualized'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
