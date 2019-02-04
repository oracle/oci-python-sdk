# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicyFilterAnswerData(object):
    """
    SteeringPolicyFilterAnswerData model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicyFilterAnswerData object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param answer_condition:
            The value to assign to the answer_condition property of this SteeringPolicyFilterAnswerData.
        :type answer_condition: str

        :param should_keep:
            The value to assign to the should_keep property of this SteeringPolicyFilterAnswerData.
        :type should_keep: bool

        """
        self.swagger_types = {
            'answer_condition': 'str',
            'should_keep': 'bool'
        }

        self.attribute_map = {
            'answer_condition': 'answerCondition',
            'should_keep': 'shouldKeep'
        }

        self._answer_condition = None
        self._should_keep = None

    @property
    def answer_condition(self):
        """
        Gets the answer_condition of this SteeringPolicyFilterAnswerData.

        :return: The answer_condition of this SteeringPolicyFilterAnswerData.
        :rtype: str
        """
        return self._answer_condition

    @answer_condition.setter
    def answer_condition(self, answer_condition):
        """
        Sets the answer_condition of this SteeringPolicyFilterAnswerData.

        :param answer_condition: The answer_condition of this SteeringPolicyFilterAnswerData.
        :type: str
        """
        self._answer_condition = answer_condition

    @property
    def should_keep(self):
        """
        Gets the should_keep of this SteeringPolicyFilterAnswerData.
        Keep the answer if the value is `true`.


        :return: The should_keep of this SteeringPolicyFilterAnswerData.
        :rtype: bool
        """
        return self._should_keep

    @should_keep.setter
    def should_keep(self, should_keep):
        """
        Sets the should_keep of this SteeringPolicyFilterAnswerData.
        Keep the answer if the value is `true`.


        :param should_keep: The should_keep of this SteeringPolicyFilterAnswerData.
        :type: bool
        """
        self._should_keep = should_keep

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
