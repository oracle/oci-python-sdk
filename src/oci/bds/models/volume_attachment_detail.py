# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VolumeAttachmentDetail(object):
    """
    A detail of the attached block volume.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VolumeAttachmentDetail object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param volume_attachment_id:
            The value to assign to the volume_attachment_id property of this VolumeAttachmentDetail.
        :type volume_attachment_id: str

        :param volume_size_in_gbs:
            The value to assign to the volume_size_in_gbs property of this VolumeAttachmentDetail.
        :type volume_size_in_gbs: int

        """
        self.swagger_types = {
            'volume_attachment_id': 'str',
            'volume_size_in_gbs': 'int'
        }

        self.attribute_map = {
            'volume_attachment_id': 'volumeAttachmentId',
            'volume_size_in_gbs': 'volumeSizeInGBs'
        }

        self._volume_attachment_id = None
        self._volume_size_in_gbs = None

    @property
    def volume_attachment_id(self):
        """
        **[Required]** Gets the volume_attachment_id of this VolumeAttachmentDetail.
        The OCID of the volume attachment.


        :return: The volume_attachment_id of this VolumeAttachmentDetail.
        :rtype: str
        """
        return self._volume_attachment_id

    @volume_attachment_id.setter
    def volume_attachment_id(self, volume_attachment_id):
        """
        Sets the volume_attachment_id of this VolumeAttachmentDetail.
        The OCID of the volume attachment.


        :param volume_attachment_id: The volume_attachment_id of this VolumeAttachmentDetail.
        :type: str
        """
        self._volume_attachment_id = volume_attachment_id

    @property
    def volume_size_in_gbs(self):
        """
        **[Required]** Gets the volume_size_in_gbs of this VolumeAttachmentDetail.
        The size of the volume in GBs.


        :return: The volume_size_in_gbs of this VolumeAttachmentDetail.
        :rtype: int
        """
        return self._volume_size_in_gbs

    @volume_size_in_gbs.setter
    def volume_size_in_gbs(self, volume_size_in_gbs):
        """
        Sets the volume_size_in_gbs of this VolumeAttachmentDetail.
        The size of the volume in GBs.


        :param volume_size_in_gbs: The volume_size_in_gbs of this VolumeAttachmentDetail.
        :type: int
        """
        self._volume_size_in_gbs = volume_size_in_gbs

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
