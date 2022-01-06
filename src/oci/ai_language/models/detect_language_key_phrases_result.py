# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DetectLanguageKeyPhrasesResult(object):
    """
    Result of a language keyPhrases detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DetectLanguageKeyPhrasesResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key_phrases:
            The value to assign to the key_phrases property of this DetectLanguageKeyPhrasesResult.
        :type key_phrases: list[oci.ai_language.models.KeyPhrase]

        """
        self.swagger_types = {
            'key_phrases': 'list[KeyPhrase]'
        }

        self.attribute_map = {
            'key_phrases': 'keyPhrases'
        }

        self._key_phrases = None

    @property
    def key_phrases(self):
        """
        **[Required]** Gets the key_phrases of this DetectLanguageKeyPhrasesResult.
        List of detected keyPhrases.


        :return: The key_phrases of this DetectLanguageKeyPhrasesResult.
        :rtype: list[oci.ai_language.models.KeyPhrase]
        """
        return self._key_phrases

    @key_phrases.setter
    def key_phrases(self, key_phrases):
        """
        Sets the key_phrases of this DetectLanguageKeyPhrasesResult.
        List of detected keyPhrases.


        :param key_phrases: The key_phrases of this DetectLanguageKeyPhrasesResult.
        :type: list[oci.ai_language.models.KeyPhrase]
        """
        self._key_phrases = key_phrases

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
