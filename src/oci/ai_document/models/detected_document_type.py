# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectedDocumentType(object):
    """
    The detected document type.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetectedDocumentType object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param document_type:
            The value to assign to the document_type property of this DetectedDocumentType.
        :type document_type: str

        :param confidence:
            The value to assign to the confidence property of this DetectedDocumentType.
        :type confidence: float

        """
        self.swagger_types = {
            'document_type': 'str',
            'confidence': 'float'
        }

        self.attribute_map = {
            'document_type': 'documentType',
            'confidence': 'confidence'
        }

        self._document_type = None
        self._confidence = None

    @property
    def document_type(self):
        """
        **[Required]** Gets the document_type of this DetectedDocumentType.
        The document type.


        :return: The document_type of this DetectedDocumentType.
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """
        Sets the document_type of this DetectedDocumentType.
        The document type.


        :param document_type: The document_type of this DetectedDocumentType.
        :type: str
        """
        self._document_type = document_type

    @property
    def confidence(self):
        """
        **[Required]** Gets the confidence of this DetectedDocumentType.
        The confidence score between 0 and 1.


        :return: The confidence of this DetectedDocumentType.
        :rtype: float
        """
        return self._confidence

    @confidence.setter
    def confidence(self, confidence):
        """
        Sets the confidence of this DetectedDocumentType.
        The confidence score between 0 and 1.


        :param confidence: The confidence of this DetectedDocumentType.
        :type: float
        """
        self._confidence = confidence

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
