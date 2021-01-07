# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MatchInfo(object):
    """
    MatchInfo
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MatchInfo object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param matching_log_entry_end_index:
            The value to assign to the matching_log_entry_end_index property of this MatchInfo.
        :type matching_log_entry_end_index: int

        :param regex_score:
            The value to assign to the regex_score property of this MatchInfo.
        :type regex_score: int

        :param step_count:
            The value to assign to the step_count property of this MatchInfo.
        :type step_count: int

        """
        self.swagger_types = {
            'matching_log_entry_end_index': 'int',
            'regex_score': 'int',
            'step_count': 'int'
        }

        self.attribute_map = {
            'matching_log_entry_end_index': 'matchingLogEntryEndIndex',
            'regex_score': 'regexScore',
            'step_count': 'stepCount'
        }

        self._matching_log_entry_end_index = None
        self._regex_score = None
        self._step_count = None

    @property
    def matching_log_entry_end_index(self):
        """
        Gets the matching_log_entry_end_index of this MatchInfo.
        matchingLogEntryEndIndex


        :return: The matching_log_entry_end_index of this MatchInfo.
        :rtype: int
        """
        return self._matching_log_entry_end_index

    @matching_log_entry_end_index.setter
    def matching_log_entry_end_index(self, matching_log_entry_end_index):
        """
        Sets the matching_log_entry_end_index of this MatchInfo.
        matchingLogEntryEndIndex


        :param matching_log_entry_end_index: The matching_log_entry_end_index of this MatchInfo.
        :type: int
        """
        self._matching_log_entry_end_index = matching_log_entry_end_index

    @property
    def regex_score(self):
        """
        Gets the regex_score of this MatchInfo.
        regexScore


        :return: The regex_score of this MatchInfo.
        :rtype: int
        """
        return self._regex_score

    @regex_score.setter
    def regex_score(self, regex_score):
        """
        Sets the regex_score of this MatchInfo.
        regexScore


        :param regex_score: The regex_score of this MatchInfo.
        :type: int
        """
        self._regex_score = regex_score

    @property
    def step_count(self):
        """
        Gets the step_count of this MatchInfo.
        stepCount


        :return: The step_count of this MatchInfo.
        :rtype: int
        """
        return self._step_count

    @step_count.setter
    def step_count(self, step_count):
        """
        Sets the step_count of this MatchInfo.
        stepCount


        :param step_count: The step_count of this MatchInfo.
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
