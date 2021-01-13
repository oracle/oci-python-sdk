# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParsedField(object):
    """
    Parsed field response.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ParsedField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param log_content:
            The value to assign to the log_content property of this ParsedField.
        :type log_content: str

        :param field_values:
            The value to assign to the field_values property of this ParsedField.
        :type field_values: list[str]

        """
        self.swagger_types = {
            'log_content': 'str',
            'field_values': 'list[str]'
        }

        self.attribute_map = {
            'log_content': 'logContent',
            'field_values': 'fieldValues'
        }

        self._log_content = None
        self._field_values = None

    @property
    def log_content(self):
        """
        Gets the log_content of this ParsedField.
        Sample log entries picked up from the given file for validation.


        :return: The log_content of this ParsedField.
        :rtype: str
        """
        return self._log_content

    @log_content.setter
    def log_content(self, log_content):
        """
        Sets the log_content of this ParsedField.
        Sample log entries picked up from the given file for validation.


        :param log_content: The log_content of this ParsedField.
        :type: str
        """
        self._log_content = log_content

    @property
    def field_values(self):
        """
        Gets the field_values of this ParsedField.
        List of field Values.


        :return: The field_values of this ParsedField.
        :rtype: list[str]
        """
        return self._field_values

    @field_values.setter
    def field_values(self, field_values):
        """
        Sets the field_values of this ParsedField.
        List of field Values.


        :param field_values: The field_values of this ParsedField.
        :type: list[str]
        """
        self._field_values = field_values

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
