# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParserTestResult(object):
    """
    ParserTestResult
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParserTestResult object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param additional_info:
            The value to assign to the additional_info property of this ParserTestResult.
        :type additional_info: dict(str, str)

        :param entries:
            The value to assign to the entries property of this ParserTestResult.
        :type entries: list[oci.log_analytics.models.AbstractParserTestResultLogEntry]

        :param example_content:
            The value to assign to the example_content property of this ParserTestResult.
        :type example_content: str

        :param lines:
            The value to assign to the lines property of this ParserTestResult.
        :type lines: list[oci.log_analytics.models.AbstractParserTestResultLogLine]

        :param named_capture_groups:
            The value to assign to the named_capture_groups property of this ParserTestResult.
        :type named_capture_groups: list[str]

        """
        self.swagger_types = {
            'additional_info': 'dict(str, str)',
            'entries': 'list[AbstractParserTestResultLogEntry]',
            'example_content': 'str',
            'lines': 'list[AbstractParserTestResultLogLine]',
            'named_capture_groups': 'list[str]'
        }

        self.attribute_map = {
            'additional_info': 'additionalInfo',
            'entries': 'entries',
            'example_content': 'exampleContent',
            'lines': 'lines',
            'named_capture_groups': 'namedCaptureGroups'
        }

        self._additional_info = None
        self._entries = None
        self._example_content = None
        self._lines = None
        self._named_capture_groups = None

    @property
    def additional_info(self):
        """
        Gets the additional_info of this ParserTestResult.
        Additional information for the test result.


        :return: The additional_info of this ParserTestResult.
        :rtype: dict(str, str)
        """
        return self._additional_info

    @additional_info.setter
    def additional_info(self, additional_info):
        """
        Sets the additional_info of this ParserTestResult.
        Additional information for the test result.


        :param additional_info: The additional_info of this ParserTestResult.
        :type: dict(str, str)
        """
        self._additional_info = additional_info

    @property
    def entries(self):
        """
        Gets the entries of this ParserTestResult.
        The test result log entries.


        :return: The entries of this ParserTestResult.
        :rtype: list[oci.log_analytics.models.AbstractParserTestResultLogEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """
        Sets the entries of this ParserTestResult.
        The test result log entries.


        :param entries: The entries of this ParserTestResult.
        :type: list[oci.log_analytics.models.AbstractParserTestResultLogEntry]
        """
        self._entries = entries

    @property
    def example_content(self):
        """
        Gets the example_content of this ParserTestResult.
        The example content.


        :return: The example_content of this ParserTestResult.
        :rtype: str
        """
        return self._example_content

    @example_content.setter
    def example_content(self, example_content):
        """
        Sets the example_content of this ParserTestResult.
        The example content.


        :param example_content: The example_content of this ParserTestResult.
        :type: str
        """
        self._example_content = example_content

    @property
    def lines(self):
        """
        Gets the lines of this ParserTestResult.
        The test result log lines.


        :return: The lines of this ParserTestResult.
        :rtype: list[oci.log_analytics.models.AbstractParserTestResultLogLine]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """
        Sets the lines of this ParserTestResult.
        The test result log lines.


        :param lines: The lines of this ParserTestResult.
        :type: list[oci.log_analytics.models.AbstractParserTestResultLogLine]
        """
        self._lines = lines

    @property
    def named_capture_groups(self):
        """
        Gets the named_capture_groups of this ParserTestResult.
        The named capture groups.


        :return: The named_capture_groups of this ParserTestResult.
        :rtype: list[str]
        """
        return self._named_capture_groups

    @named_capture_groups.setter
    def named_capture_groups(self, named_capture_groups):
        """
        Sets the named_capture_groups of this ParserTestResult.
        The named capture groups.


        :param named_capture_groups: The named_capture_groups of this ParserTestResult.
        :type: list[str]
        """
        self._named_capture_groups = named_capture_groups

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
