# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractParserTestResultLogLine(object):
    """
    AbstractParserTestResultLogLine
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractParserTestResultLogLine object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param original_log_line:
            The value to assign to the original_log_line property of this AbstractParserTestResultLogLine.
        :type original_log_line: str

        :param pre_processed_log_line:
            The value to assign to the pre_processed_log_line property of this AbstractParserTestResultLogLine.
        :type pre_processed_log_line: str

        """
        self.swagger_types = {
            'original_log_line': 'str',
            'pre_processed_log_line': 'str'
        }

        self.attribute_map = {
            'original_log_line': 'originalLogLine',
            'pre_processed_log_line': 'preProcessedLogLine'
        }

        self._original_log_line = None
        self._pre_processed_log_line = None

    @property
    def original_log_line(self):
        """
        Gets the original_log_line of this AbstractParserTestResultLogLine.
        original log line


        :return: The original_log_line of this AbstractParserTestResultLogLine.
        :rtype: str
        """
        return self._original_log_line

    @original_log_line.setter
    def original_log_line(self, original_log_line):
        """
        Sets the original_log_line of this AbstractParserTestResultLogLine.
        original log line


        :param original_log_line: The original_log_line of this AbstractParserTestResultLogLine.
        :type: str
        """
        self._original_log_line = original_log_line

    @property
    def pre_processed_log_line(self):
        """
        Gets the pre_processed_log_line of this AbstractParserTestResultLogLine.
        pre-processed log line


        :return: The pre_processed_log_line of this AbstractParserTestResultLogLine.
        :rtype: str
        """
        return self._pre_processed_log_line

    @pre_processed_log_line.setter
    def pre_processed_log_line(self, pre_processed_log_line):
        """
        Sets the pre_processed_log_line of this AbstractParserTestResultLogLine.
        pre-processed log line


        :param pre_processed_log_line: The pre_processed_log_line of this AbstractParserTestResultLogLine.
        :type: str
        """
        self._pre_processed_log_line = pre_processed_log_line

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
