# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoObjectSegment(object):
    """
    An object segment in a video.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VideoObjectSegment object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param video_segment:
            The value to assign to the video_segment property of this VideoObjectSegment.
        :type video_segment: oci.ai_vision.models.VideoSegment

        :param confidence:
            The value to assign to the confidence property of this VideoObjectSegment.
        :type confidence: float

        :param frames:
            The value to assign to the frames property of this VideoObjectSegment.
        :type frames: list[oci.ai_vision.models.VideoObjectFrame]

        """
        self.swagger_types = {
            'video_segment': 'VideoSegment',
            'confidence': 'float',
            'frames': 'list[VideoObjectFrame]'
        }

        self.attribute_map = {
            'video_segment': 'videoSegment',
            'confidence': 'confidence',
            'frames': 'frames'
        }

        self._video_segment = None
        self._confidence = None
        self._frames = None

    @property
    def video_segment(self):
        """
        **[Required]** Gets the video_segment of this VideoObjectSegment.

        :return: The video_segment of this VideoObjectSegment.
        :rtype: oci.ai_vision.models.VideoSegment
        """
        return self._video_segment

    @video_segment.setter
    def video_segment(self, video_segment):
        """
        Sets the video_segment of this VideoObjectSegment.

        :param video_segment: The video_segment of this VideoObjectSegment.
        :type: oci.ai_vision.models.VideoSegment
        """
        self._video_segment = video_segment

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this VideoObjectSegment.
        The confidence score, between 0 and 1.


        :return: The confidence of this VideoObjectSegment.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this VideoObjectSegment.
        The confidence score, between 0 and 1.


        :param confidence: The confidence of this VideoObjectSegment.
        :type: float
        """
        self._confidence = confidence

    @property
    def frames(self):
        """
        **[Required]** Gets the frames of this VideoObjectSegment.
        Object frame in a segment.


        :return: The frames of this VideoObjectSegment.
        :rtype: list[oci.ai_vision.models.VideoObjectFrame]
        """
        return self._frames

    @frames.setter
    def frames(self, frames):
        """
        Sets the frames of this VideoObjectSegment.
        Object frame in a segment.


        :param frames: The frames of this VideoObjectSegment.
        :type: list[oci.ai_vision.models.VideoObjectFrame]
        """
        self._frames = frames

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
