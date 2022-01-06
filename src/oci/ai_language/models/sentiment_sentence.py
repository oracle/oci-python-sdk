# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SentimentSentence(object):
    """
    Sentiment sentence object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SentimentSentence object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param offset:
            The value to assign to the offset property of this SentimentSentence.
        :type offset: int

        :param length:
            The value to assign to the length property of this SentimentSentence.
        :type length: int

        :param text:
            The value to assign to the text property of this SentimentSentence.
        :type text: str

        :param sentiment:
            The value to assign to the sentiment property of this SentimentSentence.
        :type sentiment: str

        :param scores:
            The value to assign to the scores property of this SentimentSentence.
        :type scores: dict(str, float)

        """
        self.swagger_types = {
            'offset': 'int',
            'length': 'int',
            'text': 'str',
            'sentiment': 'str',
            'scores': 'dict(str, float)'
        }

        self.attribute_map = {
            'offset': 'offset',
            'length': 'length',
            'text': 'text',
            'sentiment': 'sentiment',
            'scores': 'scores'
        }

        self._offset = None
        self._length = None
        self._text = None
        self._sentiment = None
        self._scores = None

    @property
    def offset(self):
        """
        Gets the offset of this SentimentSentence.
        The number of Unicode code points preceding this entity in the submitted text.


        :return: The offset of this SentimentSentence.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this SentimentSentence.
        The number of Unicode code points preceding this entity in the submitted text.


        :param offset: The offset of this SentimentSentence.
        :type: int
        """
        self._offset = offset

    @property
    def length(self):
        """
        Gets the length of this SentimentSentence.
        Length of sentence text.


        :return: The length of this SentimentSentence.
        :rtype: int
        """
        return self._length

    @length.setter
    def length(self, length):
        """
        Sets the length of this SentimentSentence.
        Length of sentence text.


        :param length: The length of this SentimentSentence.
        :type: int
        """
        self._length = length

    @property
    def text(self):
        """
        Gets the text of this SentimentSentence.
        Sentence text.


        :return: The text of this SentimentSentence.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """
        Sets the text of this SentimentSentence.
        Sentence text.


        :param text: The text of this SentimentSentence.
        :type: str
        """
        self._text = text

    @property
    def sentiment(self):
        """
        Gets the sentiment of this SentimentSentence.
        The highest-score sentiment for the sentence text.


        :return: The sentiment of this SentimentSentence.
        :rtype: str
        """
        return self._sentiment

    @sentiment.setter
    def sentiment(self, sentiment):
        """
        Sets the sentiment of this SentimentSentence.
        The highest-score sentiment for the sentence text.


        :param sentiment: The sentiment of this SentimentSentence.
        :type: str
        """
        self._sentiment = sentiment

    @property
    def scores(self):
        """
        Gets the scores of this SentimentSentence.
        Scores or confidences for each sentiment.
        Example: `{\"positive\": 1.0, \"negative\": 0.0}`


        :return: The scores of this SentimentSentence.
        :rtype: dict(str, float)
        """
        return self._scores

    @scores.setter
    def scores(self, scores):
        """
        Sets the scores of this SentimentSentence.
        Scores or confidences for each sentiment.
        Example: `{\"positive\": 1.0, \"negative\": 0.0}`


        :param scores: The scores of this SentimentSentence.
        :type: dict(str, float)
        """
        self._scores = scores

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
