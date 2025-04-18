# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20221001


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AssertionDetails(object):
    """
    The assertion details for health ner.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AssertionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this AssertionDetails.
        :type id: str

        :param type:
            The value to assign to the type property of this AssertionDetails.
        :type type: str

        :param value:
            The value to assign to the value property of this AssertionDetails.
        :type value: str

        :param score:
            The value to assign to the score property of this AssertionDetails.
        :type score: float

        """
        self.swagger_types = {
            'id': 'str',
            'type': 'str',
            'value': 'str',
            'score': 'float'
        }
        self.attribute_map = {
            'id': 'id',
            'type': 'type',
            'value': 'value',
            'score': 'score'
        }
        self._id = None
        self._type = None
        self._value = None
        self._score = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this AssertionDetails.
        id of the relation


        :return: The id of this AssertionDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AssertionDetails.
        id of the relation


        :param id: The id of this AssertionDetails.
        :type: str
        """
        self._id = id

    @property
    def type(self):
        """
        **[Required]** Gets the type of this AssertionDetails.
        type of assertion ex, Status, Certainty, Temporality, Actor, etc.


        :return: The type of this AssertionDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this AssertionDetails.
        type of assertion ex, Status, Certainty, Temporality, Actor, etc.


        :param type: The type of this AssertionDetails.
        :type: str
        """
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this AssertionDetails.
        Possible value for assertion type


        :return: The value of this AssertionDetails.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this AssertionDetails.
        Possible value for assertion type


        :param value: The value of this AssertionDetails.
        :type: str
        """
        self._value = value

    @property
    def score(self):
        """
        **[Required]** Gets the score of this AssertionDetails.
        Score or confidence for health detected entity.


        :return: The score of this AssertionDetails.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """
        Sets the score of this AssertionDetails.
        Score or confidence for health detected entity.


        :param score: The score of this AssertionDetails.
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
