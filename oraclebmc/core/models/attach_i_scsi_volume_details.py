# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.

from .attach_volume_details import AttachVolumeDetails
from ...util import formatted_flat_dict


class AttachIScsiVolumeDetails(AttachVolumeDetails):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'instance_id': 'str',
            'type': 'str',
            'volume_id': 'str',
            'use_chap': 'bool'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'type': 'type',
            'volume_id': 'volumeId',
            'use_chap': 'useChap'
        }

        self._display_name = None
        self._instance_id = None
        self._type = None
        self._volume_id = None
        self._use_chap = None
        self._type = 'iscsi'

    @property
    def use_chap(self):
        """
        Gets the use_chap of this AttachIScsiVolumeDetails.
        Whether to use CHAP authentication for the volume attachment. Defaults to false.


        :return: The use_chap of this AttachIScsiVolumeDetails.
        :rtype: bool
        """
        return self._use_chap

    @use_chap.setter
    def use_chap(self, use_chap):
        """
        Sets the use_chap of this AttachIScsiVolumeDetails.
        Whether to use CHAP authentication for the volume attachment. Defaults to false.


        :param use_chap: The use_chap of this AttachIScsiVolumeDetails.
        :type: bool
        """
        self._use_chap = use_chap

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
