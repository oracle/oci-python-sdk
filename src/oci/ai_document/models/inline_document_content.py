# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .input_location import InputLocation
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class InlineDocumentContent(InputLocation):
    """
    The content of an inline document.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new InlineDocumentContent object with values from keyword arguments. The default value of the :py:attr:`~oci.ai_document.models.InlineDocumentContent.source_type` attribute
        of this class is ``INLINE_DOCUMENT_CONTENT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param source_type:
            The value to assign to the source_type property of this InlineDocumentContent.
            Allowed values for this property are: "OBJECT_STORAGE_LOCATIONS", "INLINE_DOCUMENT_CONTENT"
        :type source_type: str

        :param data:
            The value to assign to the data property of this InlineDocumentContent.
        :type data: str

        """
        self.swagger_types = {
            'source_type': 'str',
            'data': 'str'
        }

        self.attribute_map = {
            'source_type': 'sourceType',
            'data': 'data'
        }

        self._source_type = None
        self._data = None
        self._source_type = 'INLINE_DOCUMENT_CONTENT'

    @property
    def data(self):
        """
        **[Required]** Gets the data of this InlineDocumentContent.
        Raw document data with Base64 encoding.


        :return: The data of this InlineDocumentContent.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this InlineDocumentContent.
        Raw document data with Base64 encoding.


        :param data: The data of this InlineDocumentContent.
        :type: str
        """
        self._data = data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
