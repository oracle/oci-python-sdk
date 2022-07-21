# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateStreamPackagingConfigDetails(object):
    """
    The information about the new Packaging Configuration.
    """

    #: A constant which can be used with the stream_packaging_format property of a CreateStreamPackagingConfigDetails.
    #: This constant has a value of "HLS"
    STREAM_PACKAGING_FORMAT_HLS = "HLS"

    #: A constant which can be used with the stream_packaging_format property of a CreateStreamPackagingConfigDetails.
    #: This constant has a value of "DASH"
    STREAM_PACKAGING_FORMAT_DASH = "DASH"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateStreamPackagingConfigDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param distribution_channel_id:
            The value to assign to the distribution_channel_id property of this CreateStreamPackagingConfigDetails.
        :type distribution_channel_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateStreamPackagingConfigDetails.
        :type display_name: str

        :param stream_packaging_format:
            The value to assign to the stream_packaging_format property of this CreateStreamPackagingConfigDetails.
            Allowed values for this property are: "HLS", "DASH"
        :type stream_packaging_format: str

        :param segment_time_in_seconds:
            The value to assign to the segment_time_in_seconds property of this CreateStreamPackagingConfigDetails.
        :type segment_time_in_seconds: int

        :param encryption:
            The value to assign to the encryption property of this CreateStreamPackagingConfigDetails.
        :type encryption: oci.media_services.models.StreamPackagingConfigEncryption

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateStreamPackagingConfigDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateStreamPackagingConfigDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'distribution_channel_id': 'str',
            'display_name': 'str',
            'stream_packaging_format': 'str',
            'segment_time_in_seconds': 'int',
            'encryption': 'StreamPackagingConfigEncryption',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'distribution_channel_id': 'distributionChannelId',
            'display_name': 'displayName',
            'stream_packaging_format': 'streamPackagingFormat',
            'segment_time_in_seconds': 'segmentTimeInSeconds',
            'encryption': 'encryption',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._distribution_channel_id = None
        self._display_name = None
        self._stream_packaging_format = None
        self._segment_time_in_seconds = None
        self._encryption = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def distribution_channel_id(self):
        """
        **[Required]** Gets the distribution_channel_id of this CreateStreamPackagingConfigDetails.
        Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.


        :return: The distribution_channel_id of this CreateStreamPackagingConfigDetails.
        :rtype: str
        """
        return self._distribution_channel_id

    @distribution_channel_id.setter
    def distribution_channel_id(self, distribution_channel_id):
        """
        Sets the distribution_channel_id of this CreateStreamPackagingConfigDetails.
        Unique identifier of the Distribution Channel that this stream packaging configuration belongs to.


        :param distribution_channel_id: The distribution_channel_id of this CreateStreamPackagingConfigDetails.
        :type: str
        """
        self._distribution_channel_id = distribution_channel_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateStreamPackagingConfigDetails.
        The name of the stream Packaging Configuration. Avoid entering confidential information.


        :return: The display_name of this CreateStreamPackagingConfigDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateStreamPackagingConfigDetails.
        The name of the stream Packaging Configuration. Avoid entering confidential information.


        :param display_name: The display_name of this CreateStreamPackagingConfigDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def stream_packaging_format(self):
        """
        **[Required]** Gets the stream_packaging_format of this CreateStreamPackagingConfigDetails.
        The output format for the package.

        Allowed values for this property are: "HLS", "DASH"


        :return: The stream_packaging_format of this CreateStreamPackagingConfigDetails.
        :rtype: str
        """
        return self._stream_packaging_format

    @stream_packaging_format.setter
    def stream_packaging_format(self, stream_packaging_format):
        """
        Sets the stream_packaging_format of this CreateStreamPackagingConfigDetails.
        The output format for the package.


        :param stream_packaging_format: The stream_packaging_format of this CreateStreamPackagingConfigDetails.
        :type: str
        """
        allowed_values = ["HLS", "DASH"]
        if not value_allowed_none_or_none_sentinel(stream_packaging_format, allowed_values):
            raise ValueError(
                "Invalid value for `stream_packaging_format`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._stream_packaging_format = stream_packaging_format

    @property
    def segment_time_in_seconds(self):
        """
        **[Required]** Gets the segment_time_in_seconds of this CreateStreamPackagingConfigDetails.
        The duration in seconds for each fragment.


        :return: The segment_time_in_seconds of this CreateStreamPackagingConfigDetails.
        :rtype: int
        """
        return self._segment_time_in_seconds

    @segment_time_in_seconds.setter
    def segment_time_in_seconds(self, segment_time_in_seconds):
        """
        Sets the segment_time_in_seconds of this CreateStreamPackagingConfigDetails.
        The duration in seconds for each fragment.


        :param segment_time_in_seconds: The segment_time_in_seconds of this CreateStreamPackagingConfigDetails.
        :type: int
        """
        self._segment_time_in_seconds = segment_time_in_seconds

    @property
    def encryption(self):
        """
        Gets the encryption of this CreateStreamPackagingConfigDetails.

        :return: The encryption of this CreateStreamPackagingConfigDetails.
        :rtype: oci.media_services.models.StreamPackagingConfigEncryption
        """
        return self._encryption

    @encryption.setter
    def encryption(self, encryption):
        """
        Sets the encryption of this CreateStreamPackagingConfigDetails.

        :param encryption: The encryption of this CreateStreamPackagingConfigDetails.
        :type: oci.media_services.models.StreamPackagingConfigEncryption
        """
        self._encryption = encryption

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateStreamPackagingConfigDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateStreamPackagingConfigDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateStreamPackagingConfigDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateStreamPackagingConfigDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateStreamPackagingConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateStreamPackagingConfigDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateStreamPackagingConfigDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateStreamPackagingConfigDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
