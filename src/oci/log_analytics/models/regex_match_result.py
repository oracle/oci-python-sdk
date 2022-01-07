# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RegexMatchResult(object):
    """
    RegexMatchResult
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RegexMatchResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param matched_log_entry_end_index:
            The value to assign to the matched_log_entry_end_index property of this RegexMatchResult.
        :type matched_log_entry_end_index: int

        :param regex_score:
            The value to assign to the regex_score property of this RegexMatchResult.
        :type regex_score: int

        :param regex_steps_info:
            The value to assign to the regex_steps_info property of this RegexMatchResult.
        :type regex_steps_info: list[oci.log_analytics.models.StepInfo]

        :param step_count:
            The value to assign to the step_count property of this RegexMatchResult.
        :type step_count: int

        :param sub_regexes_match_info:
            The value to assign to the sub_regexes_match_info property of this RegexMatchResult.
        :type sub_regexes_match_info: dict(str, MatchInfo)

        """
        self.swagger_types = {
            'matched_log_entry_end_index': 'int',
            'regex_score': 'int',
            'regex_steps_info': 'list[StepInfo]',
            'step_count': 'int',
            'sub_regexes_match_info': 'dict(str, MatchInfo)'
        }

        self.attribute_map = {
            'matched_log_entry_end_index': 'matchedLogEntryEndIndex',
            'regex_score': 'regexScore',
            'regex_steps_info': 'regexStepsInfo',
            'step_count': 'stepCount',
            'sub_regexes_match_info': 'subRegexesMatchInfo'
        }

        self._matched_log_entry_end_index = None
        self._regex_score = None
        self._regex_steps_info = None
        self._step_count = None
        self._sub_regexes_match_info = None

    @property
    def matched_log_entry_end_index(self):
        """
        Gets the matched_log_entry_end_index of this RegexMatchResult.
        The matched log entry end index.


        :return: The matched_log_entry_end_index of this RegexMatchResult.
        :rtype: int
        """
        return self._matched_log_entry_end_index

    @matched_log_entry_end_index.setter
    def matched_log_entry_end_index(self, matched_log_entry_end_index):
        """
        Sets the matched_log_entry_end_index of this RegexMatchResult.
        The matched log entry end index.


        :param matched_log_entry_end_index: The matched_log_entry_end_index of this RegexMatchResult.
        :type: int
        """
        self._matched_log_entry_end_index = matched_log_entry_end_index

    @property
    def regex_score(self):
        """
        Gets the regex_score of this RegexMatchResult.
        The regular expression score.


        :return: The regex_score of this RegexMatchResult.
        :rtype: int
        """
        return self._regex_score

    @regex_score.setter
    def regex_score(self, regex_score):
        """
        Sets the regex_score of this RegexMatchResult.
        The regular expression score.


        :param regex_score: The regex_score of this RegexMatchResult.
        :type: int
        """
        self._regex_score = regex_score

    @property
    def regex_steps_info(self):
        """
        Gets the regex_steps_info of this RegexMatchResult.
        The regular expression steps information.


        :return: The regex_steps_info of this RegexMatchResult.
        :rtype: list[oci.log_analytics.models.StepInfo]
        """
        return self._regex_steps_info

    @regex_steps_info.setter
    def regex_steps_info(self, regex_steps_info):
        """
        Sets the regex_steps_info of this RegexMatchResult.
        The regular expression steps information.


        :param regex_steps_info: The regex_steps_info of this RegexMatchResult.
        :type: list[oci.log_analytics.models.StepInfo]
        """
        self._regex_steps_info = regex_steps_info

    @property
    def step_count(self):
        """
        Gets the step_count of this RegexMatchResult.
        The regular expression step count.


        :return: The step_count of this RegexMatchResult.
        :rtype: int
        """
        return self._step_count

    @step_count.setter
    def step_count(self, step_count):
        """
        Sets the step_count of this RegexMatchResult.
        The regular expression step count.


        :param step_count: The step_count of this RegexMatchResult.
        :type: int
        """
        self._step_count = step_count

    @property
    def sub_regexes_match_info(self):
        """
        Gets the sub_regexes_match_info of this RegexMatchResult.
        The regular expression match information.


        :return: The sub_regexes_match_info of this RegexMatchResult.
        :rtype: dict(str, MatchInfo)
        """
        return self._sub_regexes_match_info

    @sub_regexes_match_info.setter
    def sub_regexes_match_info(self, sub_regexes_match_info):
        """
        Sets the sub_regexes_match_info of this RegexMatchResult.
        The regular expression match information.


        :param sub_regexes_match_info: The sub_regexes_match_info of this RegexMatchResult.
        :type: dict(str, MatchInfo)
        """
        self._sub_regexes_match_info = sub_regexes_match_info

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
