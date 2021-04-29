# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TextClassification(object):
    """
    Text label and score for the given text.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TextClassification object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param label:
            The value to assign to the label property of this TextClassification.
        :type label: str

        :param score:
            The value to assign to the score property of this TextClassification.
        :type score: float

        """
        self.swagger_types = {
            'label': 'str',
            'score': 'float'
        }

        self.attribute_map = {
            'label': 'label',
            'score': 'score'
        }

        self._label = None
        self._score = None

    @property
    def label(self):
        """
        **[Required]** Gets the label of this TextClassification.
        Label of the the given text.


        :return: The label of this TextClassification.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """
        Sets the label of this TextClassification.
        Label of the the given text.


        :param label: The label of this TextClassification.
        :type: str
        """
        self._label = label

    @property
    def score(self):
        """
        **[Required]** Gets the score of this TextClassification.
        Score of the given text.


        :return: The score of this TextClassification.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this TextClassification.
        Score of the given text.


        :param score: The score of this TextClassification.
        :type: float
        """
        self._score = score

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
