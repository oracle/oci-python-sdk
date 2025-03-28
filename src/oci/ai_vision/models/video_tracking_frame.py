# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20220125


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VideoTrackingFrame(object):
    """
    A frame capturing a tracked object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VideoTrackingFrame object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param time_offset_ms:
            The value to assign to the time_offset_ms property of this VideoTrackingFrame.
        :type time_offset_ms: int

        :param confidence:
            The value to assign to the confidence property of this VideoTrackingFrame.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this VideoTrackingFrame.
        :type bounding_polygon: oci.ai_vision.models.BoundingPolygon

        :param properties:
            The value to assign to the properties property of this VideoTrackingFrame.
        :type properties: list[oci.ai_vision.models.ObjectProperty]

        """
        self.swagger_types = {
            'time_offset_ms': 'int',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon',
            'properties': 'list[ObjectProperty]'
        }
        self.attribute_map = {
            'time_offset_ms': 'timeOffsetMs',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon',
            'properties': 'properties'
        }
        self._time_offset_ms = None
        self._confidence = None
        self._bounding_polygon = None
        self._properties = None

    @property
    def time_offset_ms(self):
        """
        **[Required]** Gets the time_offset_ms of this VideoTrackingFrame.
        Time offset(Milliseconds) of the frame.


        :return: The time_offset_ms of this VideoTrackingFrame.
        :rtype: int
        """
        return self._time_offset_ms

    @time_offset_ms.setter
    def time_offset_ms(self, time_offset_ms):
        """
        Sets the time_offset_ms of this VideoTrackingFrame.
        Time offset(Milliseconds) of the frame.


        :param time_offset_ms: The time_offset_ms of this VideoTrackingFrame.
        :type: int
        """
        self._time_offset_ms = time_offset_ms

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this VideoTrackingFrame.
        The confidence score, between 0 and 1.


        :return: The confidence of this VideoTrackingFrame.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this VideoTrackingFrame.
        The confidence score, between 0 and 1.


        :param confidence: The confidence of this VideoTrackingFrame.
        :type: float
        """
        self._confidence = confidence

    @property
    def bounding_polygon(self):
        """
        **[Required]** Gets the bounding_polygon of this VideoTrackingFrame.

        :return: The bounding_polygon of this VideoTrackingFrame.
        :rtype: oci.ai_vision.models.BoundingPolygon
        """
        return self._bounding_polygon

    @bounding_polygon.setter
    def bounding_polygon(self, bounding_polygon):
        """
        Sets the bounding_polygon of this VideoTrackingFrame.

        :param bounding_polygon: The bounding_polygon of this VideoTrackingFrame.
        :type: oci.ai_vision.models.BoundingPolygon
        """
        self._bounding_polygon = bounding_polygon

    @property
    def properties(self):
        """
        Gets the properties of this VideoTrackingFrame.
        Properties associated with the tracked object in the frame.


        :return: The properties of this VideoTrackingFrame.
        :rtype: list[oci.ai_vision.models.ObjectProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this VideoTrackingFrame.
        Properties associated with the tracked object in the frame.


        :param properties: The properties of this VideoTrackingFrame.
        :type: list[oci.ai_vision.models.ObjectProperty]
        """
        self._properties = properties

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
