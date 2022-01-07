# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AbstractParserTestResultLogEntry(object):
    """
    AbstractParserTestResultLogEntry
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AbstractParserTestResultLogEntry object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param extra_info_attributes:
            The value to assign to the extra_info_attributes property of this AbstractParserTestResultLogEntry.
        :type extra_info_attributes: dict(str, str)

        :param field_name_value_map:
            The value to assign to the field_name_value_map property of this AbstractParserTestResultLogEntry.
        :type field_name_value_map: dict(str, str)

        :param field_position_value_map:
            The value to assign to the field_position_value_map property of this AbstractParserTestResultLogEntry.
        :type field_position_value_map: dict(str, str)

        :param fields:
            The value to assign to the fields property of this AbstractParserTestResultLogEntry.
        :type fields: dict(str, str)

        :param log_entry:
            The value to assign to the log_entry property of this AbstractParserTestResultLogEntry.
        :type log_entry: str

        :param match_status:
            The value to assign to the match_status property of this AbstractParserTestResultLogEntry.
        :type match_status: str

        :param match_status_description:
            The value to assign to the match_status_description property of this AbstractParserTestResultLogEntry.
        :type match_status_description: str

        """
        self.swagger_types = {
            'extra_info_attributes': 'dict(str, str)',
            'field_name_value_map': 'dict(str, str)',
            'field_position_value_map': 'dict(str, str)',
            'fields': 'dict(str, str)',
            'log_entry': 'str',
            'match_status': 'str',
            'match_status_description': 'str'
        }

        self.attribute_map = {
            'extra_info_attributes': 'extraInfoAttributes',
            'field_name_value_map': 'fieldNameValueMap',
            'field_position_value_map': 'fieldPositionValueMap',
            'fields': 'fields',
            'log_entry': 'logEntry',
            'match_status': 'matchStatus',
            'match_status_description': 'matchStatusDescription'
        }

        self._extra_info_attributes = None
        self._field_name_value_map = None
        self._field_position_value_map = None
        self._fields = None
        self._log_entry = None
        self._match_status = None
        self._match_status_description = None

    @property
    def extra_info_attributes(self):
        """
        Gets the extra_info_attributes of this AbstractParserTestResultLogEntry.
        Extra information attributes.


        :return: The extra_info_attributes of this AbstractParserTestResultLogEntry.
        :rtype: dict(str, str)
        """
        return self._extra_info_attributes

    @extra_info_attributes.setter
    def extra_info_attributes(self, extra_info_attributes):
        """
        Sets the extra_info_attributes of this AbstractParserTestResultLogEntry.
        Extra information attributes.


        :param extra_info_attributes: The extra_info_attributes of this AbstractParserTestResultLogEntry.
        :type: dict(str, str)
        """
        self._extra_info_attributes = extra_info_attributes

    @property
    def field_name_value_map(self):
        """
        Gets the field_name_value_map of this AbstractParserTestResultLogEntry.
        The field name value map.


        :return: The field_name_value_map of this AbstractParserTestResultLogEntry.
        :rtype: dict(str, str)
        """
        return self._field_name_value_map

    @field_name_value_map.setter
    def field_name_value_map(self, field_name_value_map):
        """
        Sets the field_name_value_map of this AbstractParserTestResultLogEntry.
        The field name value map.


        :param field_name_value_map: The field_name_value_map of this AbstractParserTestResultLogEntry.
        :type: dict(str, str)
        """
        self._field_name_value_map = field_name_value_map

    @property
    def field_position_value_map(self):
        """
        Gets the field_position_value_map of this AbstractParserTestResultLogEntry.
        The field position value map.


        :return: The field_position_value_map of this AbstractParserTestResultLogEntry.
        :rtype: dict(str, str)
        """
        return self._field_position_value_map

    @field_position_value_map.setter
    def field_position_value_map(self, field_position_value_map):
        """
        Sets the field_position_value_map of this AbstractParserTestResultLogEntry.
        The field position value map.


        :param field_position_value_map: The field_position_value_map of this AbstractParserTestResultLogEntry.
        :type: dict(str, str)
        """
        self._field_position_value_map = field_position_value_map

    @property
    def fields(self):
        """
        Gets the fields of this AbstractParserTestResultLogEntry.
        The parser fields.


        :return: The fields of this AbstractParserTestResultLogEntry.
        :rtype: dict(str, str)
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """
        Sets the fields of this AbstractParserTestResultLogEntry.
        The parser fields.


        :param fields: The fields of this AbstractParserTestResultLogEntry.
        :type: dict(str, str)
        """
        self._fields = fields

    @property
    def log_entry(self):
        """
        Gets the log_entry of this AbstractParserTestResultLogEntry.
        The log entry.


        :return: The log_entry of this AbstractParserTestResultLogEntry.
        :rtype: str
        """
        return self._log_entry

    @log_entry.setter
    def log_entry(self, log_entry):
        """
        Sets the log_entry of this AbstractParserTestResultLogEntry.
        The log entry.


        :param log_entry: The log_entry of this AbstractParserTestResultLogEntry.
        :type: str
        """
        self._log_entry = log_entry

    @property
    def match_status(self):
        """
        Gets the match_status of this AbstractParserTestResultLogEntry.
        The match status.


        :return: The match_status of this AbstractParserTestResultLogEntry.
        :rtype: str
        """
        return self._match_status

    @match_status.setter
    def match_status(self, match_status):
        """
        Sets the match_status of this AbstractParserTestResultLogEntry.
        The match status.


        :param match_status: The match_status of this AbstractParserTestResultLogEntry.
        :type: str
        """
        self._match_status = match_status

    @property
    def match_status_description(self):
        """
        Gets the match_status_description of this AbstractParserTestResultLogEntry.
        The match status description.


        :return: The match_status_description of this AbstractParserTestResultLogEntry.
        :rtype: str
        """
        return self._match_status_description

    @match_status_description.setter
    def match_status_description(self, match_status_description):
        """
        Sets the match_status_description of this AbstractParserTestResultLogEntry.
        The match status description.


        :param match_status_description: The match_status_description of this AbstractParserTestResultLogEntry.
        :type: str
        """
        self._match_status_description = match_status_description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
