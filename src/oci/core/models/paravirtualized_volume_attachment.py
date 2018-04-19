# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.

from .volume_attachment import VolumeAttachment
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParavirtualizedVolumeAttachment(VolumeAttachment):
    """
    A paravirtualized volume attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParavirtualizedVolumeAttachment object with values from keyword arguments. The default value of the :py:attr:`~oci.core.models.ParavirtualizedVolumeAttachment.attachment_type` attribute
        of this class is ``paravirtualized`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param attachment_type:
            The value to assign to the attachment_type property of this ParavirtualizedVolumeAttachment.
        :type attachment_type: str

        :param availability_domain:
            The value to assign to the availability_domain property of this ParavirtualizedVolumeAttachment.
        :type availability_domain: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ParavirtualizedVolumeAttachment.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this ParavirtualizedVolumeAttachment.
        :type display_name: str

        :param id:
            The value to assign to the id property of this ParavirtualizedVolumeAttachment.
        :type id: str

        :param instance_id:
            The value to assign to the instance_id property of this ParavirtualizedVolumeAttachment.
        :type instance_id: str

        :param is_read_only:
            The value to assign to the is_read_only property of this ParavirtualizedVolumeAttachment.
        :type is_read_only: bool

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ParavirtualizedVolumeAttachment.
            Allowed values for this property are: "ATTACHING", "ATTACHED", "DETACHING", "DETACHED"
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this ParavirtualizedVolumeAttachment.
        :type time_created: datetime

        :param volume_id:
            The value to assign to the volume_id property of this ParavirtualizedVolumeAttachment.
        :type volume_id: str

        """
        self.swagger_types = {
            'attachment_type': 'str',
            'availability_domain': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'id': 'str',
            'instance_id': 'str',
            'is_read_only': 'bool',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'volume_id': 'str'
        }

        self.attribute_map = {
            'attachment_type': 'attachmentType',
            'availability_domain': 'availabilityDomain',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'id': 'id',
            'instance_id': 'instanceId',
            'is_read_only': 'isReadOnly',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'volume_id': 'volumeId'
        }

        self._attachment_type = None
        self._availability_domain = None
        self._compartment_id = None
        self._display_name = None
        self._id = None
        self._instance_id = None
        self._is_read_only = None
        self._lifecycle_state = None
        self._time_created = None
        self._volume_id = None
        self._attachment_type = 'paravirtualized'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
