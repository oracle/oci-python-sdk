# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .attach_volume_details import AttachVolumeDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AttachServiceDeterminedVolumeDetails(AttachVolumeDetails):
    """
    AttachServiceDeterminedVolumeDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AttachServiceDeterminedVolumeDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.AttachServiceDeterminedVolumeDetails.type` attribute
        of this class is ``service_determined`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param device:
            The value to assign to the device property of this AttachServiceDeterminedVolumeDetails.
        :type device: str

        :param display_name:
            The value to assign to the display_name property of this AttachServiceDeterminedVolumeDetails.
        :type display_name: str

        :param instance_id:
            The value to assign to the instance_id property of this AttachServiceDeterminedVolumeDetails.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this AttachServiceDeterminedVolumeDetails.
        :type is_read_only: bool

        :param is_shareable:
            The value to assign to the is_shareable property of this AttachServiceDeterminedVolumeDetails.
        :type is_shareable: bool

        :param type:
            The value to assign to the type property of this AttachServiceDeterminedVolumeDetails.
        :type type: str

        :param volume_id:
            The value to assign to the volume_id property of this AttachServiceDeterminedVolumeDetails.
        :type volume_id: str

        """
        self.swagger_types = {
            'device': 'str',
            'display_name': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
            'is_shareable': 'bool',
            'type': 'str',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'device': 'device',
            'display_name': 'displayName',
            'instance_id': 'instanceId',
            'is_read_only': 'isReadOnly',
            'is_shareable': 'isShareable',
            'type': 'type',
            'volume_id': 'volumeId'
        }

        self._device = None
        self._display_name = None
        self._instance_id = None
        self._is_read_only = None
        self._is_shareable = None
        self._type = None
        self._volume_id = None
        self._type = 'service_determined'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
