# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .stream_packaging_config import StreamPackagingConfig
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class HlsStreamPackagingConfig(StreamPackagingConfig):
    """
    Configuration fields for a HLS Packaging Configuration.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new HlsStreamPackagingConfig object with values from keyword arguments. The default value of the :py:attr:`~oci.media_services.models.HlsStreamPackagingConfig.stream_packaging_format` attribute
        of this class is ``HLS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this HlsStreamPackagingConfig.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this HlsStreamPackagingConfig.
        :type compartment_id: str

        :param distribution_channel_id:
            The value to assign to the distribution_channel_id property of this HlsStreamPackagingConfig.
        :type distribution_channel_id: str

        :param display_name:
            The value to assign to the display_name property of this HlsStreamPackagingConfig.
        :type display_name: str

        :param stream_packaging_format:
            The value to assign to the stream_packaging_format property of this HlsStreamPackagingConfig.
            Allowed values for this property are: "HLS", "DASH"
        :type stream_packaging_format: str

        :param segment_time_in_seconds:
            The value to assign to the segment_time_in_seconds property of this HlsStreamPackagingConfig.
        :type segment_time_in_seconds: int

        :param encryption:
            The value to assign to the encryption property of this HlsStreamPackagingConfig.
        :type encryption: oci.media_services.models.StreamPackagingConfigEncryption

        :param time_created:
            The value to assign to the time_created property of this HlsStreamPackagingConfig.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this HlsStreamPackagingConfig.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this HlsStreamPackagingConfig.
            Allowed values for this property are: "ACTIVE", "NEEDS_ATTENTION", "DELETED"
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this HlsStreamPackagingConfig.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this HlsStreamPackagingConfig.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this HlsStreamPackagingConfig.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'distribution_channel_id': 'str',
            'display_name': 'str',
            'stream_packaging_format': 'str',
            'segment_time_in_seconds': 'int',
            'encryption': 'StreamPackagingConfigEncryption',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'distribution_channel_id': 'distributionChannelId',
            'display_name': 'displayName',
            'stream_packaging_format': 'streamPackagingFormat',
            'segment_time_in_seconds': 'segmentTimeInSeconds',
            'encryption': 'encryption',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._distribution_channel_id = None
        self._display_name = None
        self._stream_packaging_format = None
        self._segment_time_in_seconds = None
        self._encryption = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._stream_packaging_format = 'HLS'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
