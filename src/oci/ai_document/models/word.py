# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Word(object):
    """
    A single word.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Word object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param text:
            The value to assign to the text property of this Word.
        :type text: str

        :param confidence:
            The value to assign to the confidence property of this Word.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this Word.
        :type bounding_polygon: oci.ai_document.models.BoundingPolygon

        """
        self.swagger_types = {
            'text': 'str',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon'
        }

        self.attribute_map = {
            'text': 'text',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon'
        }

        self._text = None
        self._confidence = None
        self._bounding_polygon = None

    @property
    def text(self):
        """
        **[Required]** Gets the text of this Word.
        The string of text characters in the word.


        :return: The text of this Word.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this Word.
        The string of text characters in the word.


        :param text: The text of this Word.
        :type: str
        """
        self._text = text

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this Word.
        the confidence score between 0 and 1.


        :return: The confidence of this Word.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this Word.
        the confidence score between 0 and 1.


        :param confidence: The confidence of this Word.
        :type: float
        """
        self._confidence = confidence

    @property
    def bounding_polygon(self):
        """
        **[Required]** Gets the bounding_polygon of this Word.

        :return: The bounding_polygon of this Word.
        :rtype: oci.ai_document.models.BoundingPolygon
        """
        return self._bounding_polygon

    @bounding_polygon.setter
    def bounding_polygon(self, bounding_polygon):
        """
        Sets the bounding_polygon of this Word.

        :param bounding_polygon: The bounding_polygon of this Word.
        :type: oci.ai_document.models.BoundingPolygon
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
