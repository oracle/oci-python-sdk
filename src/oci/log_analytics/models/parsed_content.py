# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParsedContent(object):
    """
    Parsed representation of the log file.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParsedContent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_names:
            The value to assign to the field_names property of this ParsedContent.
        :type field_names: list[str]

        :param field_display_names:
            The value to assign to the field_display_names property of this ParsedContent.
        :type field_display_names: list[str]

        :param parsed_field_values:
            The value to assign to the parsed_field_values property of this ParsedContent.
        :type parsed_field_values: list[oci.log_analytics.models.ParsedField]

        :param log_content:
            The value to assign to the log_content property of this ParsedContent.
        :type log_content: str

        :param sample_size:
            The value to assign to the sample_size property of this ParsedContent.
        :type sample_size: int

        :param match_status:
            The value to assign to the match_status property of this ParsedContent.
        :type match_status: str

        """
        self.swagger_types = {
            'field_names': 'list[str]',
            'field_display_names': 'list[str]',
            'parsed_field_values': 'list[ParsedField]',
            'log_content': 'str',
            'sample_size': 'int',
            'match_status': 'str'
        }

        self.attribute_map = {
            'field_names': 'fieldNames',
            'field_display_names': 'fieldDisplayNames',
            'parsed_field_values': 'parsedFieldValues',
            'log_content': 'logContent',
            'sample_size': 'sampleSize',
            'match_status': 'matchStatus'
        }

        self._field_names = None
        self._field_display_names = None
        self._parsed_field_values = None
        self._log_content = None
        self._sample_size = None
        self._match_status = None

    @property
    def field_names(self):
        """
        Gets the field_names of this ParsedContent.
        List of field names.


        :return: The field_names of this ParsedContent.
        :rtype: list[str]
        """
        return self._field_names

    @field_names.setter
    def field_names(self, field_names):
        """
        Sets the field_names of this ParsedContent.
        List of field names.


        :param field_names: The field_names of this ParsedContent.
        :type: list[str]
        """
        self._field_names = field_names

    @property
    def field_display_names(self):
        """
        Gets the field_display_names of this ParsedContent.
        List of field display names.


        :return: The field_display_names of this ParsedContent.
        :rtype: list[str]
        """
        return self._field_display_names

    @field_display_names.setter
    def field_display_names(self, field_display_names):
        """
        Sets the field_display_names of this ParsedContent.
        List of field display names.


        :param field_display_names: The field_display_names of this ParsedContent.
        :type: list[str]
        """
        self._field_display_names = field_display_names

    @property
    def parsed_field_values(self):
        """
        Gets the parsed_field_values of this ParsedContent.
        Parsed field values.


        :return: The parsed_field_values of this ParsedContent.
        :rtype: list[oci.log_analytics.models.ParsedField]
        """
        return self._parsed_field_values

    @parsed_field_values.setter
    def parsed_field_values(self, parsed_field_values):
        """
        Sets the parsed_field_values of this ParsedContent.
        Parsed field values.


        :param parsed_field_values: The parsed_field_values of this ParsedContent.
        :type: list[oci.log_analytics.models.ParsedField]
        """
        self._parsed_field_values = parsed_field_values

    @property
    def log_content(self):
        """
        Gets the log_content of this ParsedContent.
        Sample log entries picked up from the given file for validation.


        :return: The log_content of this ParsedContent.
        :rtype: str
        """
        return self._log_content

    @log_content.setter
    def log_content(self, log_content):
        """
        Sets the log_content of this ParsedContent.
        Sample log entries picked up from the given file for validation.


        :param log_content: The log_content of this ParsedContent.
        :type: str
        """
        self._log_content = log_content

    @property
    def sample_size(self):
        """
        Gets the sample_size of this ParsedContent.
        Sample Size taken for validation.


        :return: The sample_size of this ParsedContent.
        :rtype: int
        """
        return self._sample_size

    @sample_size.setter
    def sample_size(self, sample_size):
        """
        Sets the sample_size of this ParsedContent.
        Sample Size taken for validation.


        :param sample_size: The sample_size of this ParsedContent.
        :type: int
        """
        self._sample_size = sample_size

    @property
    def match_status(self):
        """
        Gets the match_status of this ParsedContent.
        Match Status.


        :return: The match_status of this ParsedContent.
        :rtype: str
        """
        return self._match_status

    @match_status.setter
    def match_status(self, match_status):
        """
        Sets the match_status of this ParsedContent.
        Match Status.


        :param match_status: The match_status of this ParsedContent.
        :type: str
        """
        self._match_status = match_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
