# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class StepInfo(object):
    """
    StepInfo
    """

    def __init__(self, **kwargs):
        """
        Initializes a new StepInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param input_sequence_current_match:
            The value to assign to the input_sequence_current_match property of this StepInfo.
        :type input_sequence_current_match: str

        :param regex_engine_class_name:
            The value to assign to the regex_engine_class_name property of this StepInfo.
        :type regex_engine_class_name: str

        :param step_count:
            The value to assign to the step_count property of this StepInfo.
        :type step_count: int

        """
        self.swagger_types = {
            'input_sequence_current_match': 'str',
            'regex_engine_class_name': 'str',
            'step_count': 'int'
        }

        self.attribute_map = {
            'input_sequence_current_match': 'inputSequenceCurrentMatch',
            'regex_engine_class_name': 'regexEngineClassName',
            'step_count': 'stepCount'
        }

        self._input_sequence_current_match = None
        self._regex_engine_class_name = None
        self._step_count = None

    @property
    def input_sequence_current_match(self):
        """
        Gets the input_sequence_current_match of this StepInfo.
        The currnet input sequence match.


        :return: The input_sequence_current_match of this StepInfo.
        :rtype: str
        """
        return self._input_sequence_current_match

    @input_sequence_current_match.setter
    def input_sequence_current_match(self, input_sequence_current_match):
        """
        Sets the input_sequence_current_match of this StepInfo.
        The currnet input sequence match.


        :param input_sequence_current_match: The input_sequence_current_match of this StepInfo.
        :type: str
        """
        self._input_sequence_current_match = input_sequence_current_match

    @property
    def regex_engine_class_name(self):
        """
        Gets the regex_engine_class_name of this StepInfo.
        The regular expression engine class name.


        :return: The regex_engine_class_name of this StepInfo.
        :rtype: str
        """
        return self._regex_engine_class_name

    @regex_engine_class_name.setter
    def regex_engine_class_name(self, regex_engine_class_name):
        """
        Sets the regex_engine_class_name of this StepInfo.
        The regular expression engine class name.


        :param regex_engine_class_name: The regex_engine_class_name of this StepInfo.
        :type: str
        """
        self._regex_engine_class_name = regex_engine_class_name

    @property
    def step_count(self):
        """
        Gets the step_count of this StepInfo.
        The step count.


        :return: The step_count of this StepInfo.
        :rtype: int
        """
        return self._step_count

    @step_count.setter
    def step_count(self, step_count):
        """
        Sets the step_count of this StepInfo.
        The step count.


        :param step_count: The step_count of this StepInfo.
        :type: int
        """
        self._step_count = step_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
