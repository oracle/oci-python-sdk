# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SentimentDocumentResult(object):
    """
    The document response for sentiment detect call.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SentimentDocumentResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this SentimentDocumentResult.
        :type key: str

        :param document_sentiment:
            The value to assign to the document_sentiment property of this SentimentDocumentResult.
        :type document_sentiment: str

        :param document_scores:
            The value to assign to the document_scores property of this SentimentDocumentResult.
        :type document_scores: dict(str, float)

        :param aspects:
            The value to assign to the aspects property of this SentimentDocumentResult.
        :type aspects: list[oci.ai_language.models.SentimentAspect]

        :param sentences:
            The value to assign to the sentences property of this SentimentDocumentResult.
        :type sentences: list[oci.ai_language.models.SentimentSentence]

        :param language_code:
            The value to assign to the language_code property of this SentimentDocumentResult.
        :type language_code: str

        """
        self.swagger_types = {
            'key': 'str',
            'document_sentiment': 'str',
            'document_scores': 'dict(str, float)',
            'aspects': 'list[SentimentAspect]',
            'sentences': 'list[SentimentSentence]',
            'language_code': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'document_sentiment': 'documentSentiment',
            'document_scores': 'documentScores',
            'aspects': 'aspects',
            'sentences': 'sentences',
            'language_code': 'languageCode'
        }

        self._key = None
        self._document_sentiment = None
        self._document_scores = None
        self._aspects = None
        self._sentences = None
        self._language_code = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this SentimentDocumentResult.
        Document unique identifier defined by the user.


        :return: The key of this SentimentDocumentResult.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this SentimentDocumentResult.
        Document unique identifier defined by the user.


        :param key: The key of this SentimentDocumentResult.
        :type: str
        """
        self._key = key

    @property
    def document_sentiment(self):
        """
        Gets the document_sentiment of this SentimentDocumentResult.
        Document level sentiment.


        :return: The document_sentiment of this SentimentDocumentResult.
        :rtype: str
        """
        return self._document_sentiment

    @document_sentiment.setter
    def document_sentiment(self, document_sentiment):
        """
        Sets the document_sentiment of this SentimentDocumentResult.
        Document level sentiment.


        :param document_sentiment: The document_sentiment of this SentimentDocumentResult.
        :type: str
        """
        self._document_sentiment = document_sentiment

    @property
    def document_scores(self):
        """
        Gets the document_scores of this SentimentDocumentResult.
        Scores for each sentiment.
        Example: {\"positive\": 1.0, \"negative\": 0.0}


        :return: The document_scores of this SentimentDocumentResult.
        :rtype: dict(str, float)
        """
        return self._document_scores

    @document_scores.setter
    def document_scores(self, document_scores):
        """
        Sets the document_scores of this SentimentDocumentResult.
        Scores for each sentiment.
        Example: {\"positive\": 1.0, \"negative\": 0.0}


        :param document_scores: The document_scores of this SentimentDocumentResult.
        :type: dict(str, float)
        """
        self._document_scores = document_scores

    @property
    def aspects(self):
        """
        **[Required]** Gets the aspects of this SentimentDocumentResult.
        List of detected aspects sentiment.


        :return: The aspects of this SentimentDocumentResult.
        :rtype: list[oci.ai_language.models.SentimentAspect]
        """
        return self._aspects

    @aspects.setter
    def aspects(self, aspects):
        """
        Sets the aspects of this SentimentDocumentResult.
        List of detected aspects sentiment.


        :param aspects: The aspects of this SentimentDocumentResult.
        :type: list[oci.ai_language.models.SentimentAspect]
        """
        self._aspects = aspects

    @property
    def sentences(self):
        """
        Gets the sentences of this SentimentDocumentResult.
        List of detected sentences sentiment.


        :return: The sentences of this SentimentDocumentResult.
        :rtype: list[oci.ai_language.models.SentimentSentence]
        """
        return self._sentences

    @sentences.setter
    def sentences(self, sentences):
        """
        Sets the sentences of this SentimentDocumentResult.
        List of detected sentences sentiment.


        :param sentences: The sentences of this SentimentDocumentResult.
        :type: list[oci.ai_language.models.SentimentSentence]
        """
        self._sentences = sentences

    @property
    def language_code(self):
        """
        **[Required]** Gets the language_code of this SentimentDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :return: The language_code of this SentimentDocumentResult.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """
        Sets the language_code of this SentimentDocumentResult.
        Language code per the `ISO 639-1`__ standard.

        __ https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes


        :param language_code: The language_code of this SentimentDocumentResult.
        :type: str
        """
        self._language_code = language_code

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
