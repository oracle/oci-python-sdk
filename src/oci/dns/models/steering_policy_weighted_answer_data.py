# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyWeightedAnswerData(object):
    """
    SteeringPolicyWeightedAnswerData model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyWeightedAnswerData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param answer_condition:
            The value to assign to the answer_condition property of this SteeringPolicyWeightedAnswerData.
        :type answer_condition: str

        :param value:
            The value to assign to the value property of this SteeringPolicyWeightedAnswerData.
        :type value: int

        """
        self.swagger_types = {
            'answer_condition': 'str',
            'value': 'int'
        }

        self.attribute_map = {
            'answer_condition': 'answerCondition',
            'value': 'value'
        }

        self._answer_condition = None
        self._value = None

    @property
    def answer_condition(self):
        """
        Gets the answer_condition of this SteeringPolicyWeightedAnswerData.

        :return: The answer_condition of this SteeringPolicyWeightedAnswerData.
        :rtype: str
        """
        return self._answer_condition

    @answer_condition.setter
    def answer_condition(self, answer_condition):
        """
        Sets the answer_condition of this SteeringPolicyWeightedAnswerData.

        :param answer_condition: The answer_condition of this SteeringPolicyWeightedAnswerData.
        :type: str
        """
        self._answer_condition = answer_condition

    @property
    def value(self):
        """
        Gets the value of this SteeringPolicyWeightedAnswerData.

        :return: The value of this SteeringPolicyWeightedAnswerData.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SteeringPolicyWeightedAnswerData.

        :param value: The value of this SteeringPolicyWeightedAnswerData.
        :type: int
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
