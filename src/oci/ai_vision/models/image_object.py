# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ImageObject(object):
    """
    The object detected in an image.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ImageObject object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ImageObject.
        :type name: str

        :param confidence:
            The value to assign to the confidence property of this ImageObject.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this ImageObject.
        :type bounding_polygon: oci.ai_vision.models.BoundingPolygon

        """
        self.swagger_types = {
            'name': 'str',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon'
        }

        self.attribute_map = {
            'name': 'name',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon'
        }

        self._name = None
        self._confidence = None
        self._bounding_polygon = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ImageObject.
        The object category name. Every value returned by the pre-deployed model is in English.


        :return: The name of this ImageObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ImageObject.
        The object category name. Every value returned by the pre-deployed model is in English.


        :param name: The name of this ImageObject.
        :type: str
        """
        self._name = name

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this ImageObject.
        The confidence score, between 0 and 1.


        :return: The confidence of this ImageObject.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this ImageObject.
        The confidence score, between 0 and 1.


        :param confidence: The confidence of this ImageObject.
        :type: float
        """
        self._confidence = confidence

    @property
    def bounding_polygon(self):
        """
        **[Required]** Gets the bounding_polygon of this ImageObject.

        :return: The bounding_polygon of this ImageObject.
        :rtype: oci.ai_vision.models.BoundingPolygon
        """
        return self._bounding_polygon

    @bounding_polygon.setter
    def bounding_polygon(self, bounding_polygon):
        """
        Sets the bounding_polygon of this ImageObject.

        :param bounding_polygon: The bounding_polygon of this ImageObject.
        :type: oci.ai_vision.models.BoundingPolygon
        """
        self._bounding_polygon = bounding_polygon

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
