# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .field_value import FieldValue
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ValueArray(FieldValue):
    """
    Array of field values.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ValueArray object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_vision.models.ValueArray.value_type` attribute
        of this class is ``ARRAY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value_type:
            The value to assign to the value_type property of this ValueArray.
            Allowed values for this property are: "STRING", "DATE", "TIME", "PHONE_NUMBER", "NUMBER", "INTEGER", "ARRAY"
        :type value_type: str

        :param text:
            The value to assign to the text property of this ValueArray.
        :type text: str

        :param confidence:
            The value to assign to the confidence property of this ValueArray.
        :type confidence: float

        :param bounding_polygon:
            The value to assign to the bounding_polygon property of this ValueArray.
        :type bounding_polygon: oci.ai_vision.models.BoundingPolygon

        :param word_indexes:
            The value to assign to the word_indexes property of this ValueArray.
        :type word_indexes: list[int]

        :param items:
            The value to assign to the items property of this ValueArray.
        :type items: list[oci.ai_vision.models.DocumentField]

        """
        self.swagger_types = {
            'value_type': 'str',
            'text': 'str',
            'confidence': 'float',
            'bounding_polygon': 'BoundingPolygon',
            'word_indexes': 'list[int]',
            'items': 'list[DocumentField]'
        }

        self.attribute_map = {
            'value_type': 'valueType',
            'text': 'text',
            'confidence': 'confidence',
            'bounding_polygon': 'boundingPolygon',
            'word_indexes': 'wordIndexes',
            'items': 'items'
        }

        self._value_type = None
        self._text = None
        self._confidence = None
        self._bounding_polygon = None
        self._word_indexes = None
        self._items = None
        self._value_type = 'ARRAY'

    @property
    def items(self):
        """
        **[Required]** Gets the items of this ValueArray.

        :return: The items of this ValueArray.
        :rtype: list[oci.ai_vision.models.DocumentField]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this ValueArray.

        :param items: The items of this ValueArray.
        :type: list[oci.ai_vision.models.DocumentField]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
