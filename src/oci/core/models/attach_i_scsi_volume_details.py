# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .attach_volume_details import AttachVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachIScsiVolumeDetails(AttachVolumeDetails):
    """
    AttachIScsiVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachIScsiVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.AttachIScsiVolumeDetails.type` attribute
        of this class is ``iscsi`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param device:
            The value to assign to the device property of this AttachIScsiVolumeDetails.
        :type device: str

        :param display_name:
            The value to assign to the display_name property of this AttachIScsiVolumeDetails.
        :type display_name: str

        :param instance_id:
            The value to assign to the instance_id property of this AttachIScsiVolumeDetails.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this AttachIScsiVolumeDetails.
        :type is_read_only: bool

        :param is_shareable:
            The value to assign to the is_shareable property of this AttachIScsiVolumeDetails.
        :type is_shareable: bool

        :param type:
            The value to assign to the type property of this AttachIScsiVolumeDetails.
        :type type: str

        :param volume_id:
            The value to assign to the volume_id property of this AttachIScsiVolumeDetails.
        :type volume_id: str

        :param use_chap:
            The value to assign to the use_chap property of this AttachIScsiVolumeDetails.
        :type use_chap: bool

        """
        self.swagger_types = {
            'device': 'str',
            'display_name': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
            'is_shareable': 'bool',
            'type': 'str',
            'volume_id': 'str',
            'use_chap': 'bool'
        }

        self.attribute_map = {
            'device': 'device',
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'is_read_only': 'isReadOnly',
            'is_shareable': 'isShareable',
            'type': 'type',
            'volume_id': 'volumeId',
            'use_chap': 'useChap'
        }

        self._device = None
        self._display_name = None
        self._instance_id = None
        self._is_read_only = None
        self._is_shareable = None
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
