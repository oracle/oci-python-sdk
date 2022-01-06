# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DominantLanguageDocument(object):
    """
    The document details for language detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DominantLanguageDocument object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this DominantLanguageDocument.
        :type key: str

        :param text:
            The value to assign to the text property of this DominantLanguageDocument.
        :type text: str

        """
        self.swagger_types = {
            'key': 'str',
            'text': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'text': 'text'
        }

        self._key = None
        self._text = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this DominantLanguageDocument.
        Document unique identifier defined by the user.


        :return: The key of this DominantLanguageDocument.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this DominantLanguageDocument.
        Document unique identifier defined by the user.


        :param key: The key of this DominantLanguageDocument.
        :type: str
        """
        self._key = key

    @property
    def text(self):
        """
        **[Required]** Gets the text of this DominantLanguageDocument.
        Document text for detect language.


        :return: The text of this DominantLanguageDocument.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this DominantLanguageDocument.
        Document text for detect language.


        :param text: The text of this DominantLanguageDocument.
        :type: str
        """
        self._text = text

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
