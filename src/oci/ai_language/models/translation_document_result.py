# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TranslationDocumentResult(object):
    """
    The document response for translation call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TranslationDocumentResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this TranslationDocumentResult.
        :type key: str

        :param translated_text:
            The value to assign to the translated_text property of this TranslationDocumentResult.
        :type translated_text: str

        :param source_language_code:
            The value to assign to the source_language_code property of this TranslationDocumentResult.
        :type source_language_code: str

        :param target_language_code:
            The value to assign to the target_language_code property of this TranslationDocumentResult.
        :type target_language_code: str

        """
        self.swagger_types = {
            'key': 'str',
            'translated_text': 'str',
            'source_language_code': 'str',
            'target_language_code': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'translated_text': 'translatedText',
            'source_language_code': 'sourceLanguageCode',
            'target_language_code': 'targetLanguageCode'
        }

        self._key = None
        self._translated_text = None
        self._source_language_code = None
        self._target_language_code = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this TranslationDocumentResult.
        Document unique identifier defined by the user.


        :return: The key of this TranslationDocumentResult.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this TranslationDocumentResult.
        Document unique identifier defined by the user.


        :param key: The key of this TranslationDocumentResult.
        :type: str
        """
        self._key = key

    @property
    def translated_text(self):
        """
        **[Required]** Gets the translated_text of this TranslationDocumentResult.
        Translated text in selected target language.


        :return: The translated_text of this TranslationDocumentResult.
        :rtype: str
        """
        return self._translated_text

    @translated_text.setter
    def translated_text(self, translated_text):
        """
        Sets the translated_text of this TranslationDocumentResult.
        Translated text in selected target language.


        :param translated_text: The translated_text of this TranslationDocumentResult.
        :type: str
        """
        self._translated_text = translated_text

    @property
    def source_language_code(self):
        """
        **[Required]** Gets the source_language_code of this TranslationDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :return: The source_language_code of this TranslationDocumentResult.
        :rtype: str
        """
        return self._source_language_code

    @source_language_code.setter
    def source_language_code(self, source_language_code):
        """
        Sets the source_language_code of this TranslationDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :param source_language_code: The source_language_code of this TranslationDocumentResult.
        :type: str
        """
        self._source_language_code = source_language_code

    @property
    def target_language_code(self):
        """
        **[Required]** Gets the target_language_code of this TranslationDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :return: The target_language_code of this TranslationDocumentResult.
        :rtype: str
        """
        return self._target_language_code

    @target_language_code.setter
    def target_language_code(self, target_language_code):
        """
        Sets the target_language_code of this TranslationDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :param target_language_code: The target_language_code of this TranslationDocumentResult.
        :type: str
        """
        self._target_language_code = target_language_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
