# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GrokPattern(object):
    """
    grok pattern object.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new GrokPattern object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param pattern:
            The value to assign to the pattern property of this GrokPattern.
        :type pattern: str

        :param name:
            The value to assign to the name property of this GrokPattern.
        :type name: str

        :param field_time_key:
            The value to assign to the field_time_key property of this GrokPattern.
        :type field_time_key: str

        :param field_time_format:
            The value to assign to the field_time_format property of this GrokPattern.
        :type field_time_format: str

        :param field_time_zone:
            The value to assign to the field_time_zone property of this GrokPattern.
        :type field_time_zone: str

        """
        self.swagger_types = {
            'pattern': 'str',
            'name': 'str',
            'field_time_key': 'str',
            'field_time_format': 'str',
            'field_time_zone': 'str'
        }

        self.attribute_map = {
            'pattern': 'pattern',
            'name': 'name',
            'field_time_key': 'fieldTimeKey',
            'field_time_format': 'fieldTimeFormat',
            'field_time_zone': 'fieldTimeZone'
        }

        self._pattern = None
        self._name = None
        self._field_time_key = None
        self._field_time_format = None
        self._field_time_zone = None

    @property
    def pattern(self):
        """
        **[Required]** Gets the pattern of this GrokPattern.
        The grok pattern.


        :return: The pattern of this GrokPattern.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this GrokPattern.
        The grok pattern.


        :param pattern: The pattern of this GrokPattern.
        :type: str
        """
        self._pattern = pattern

    @property
    def name(self):
        """
        Gets the name of this GrokPattern.
        The name key to tag this grok pattern.


        :return: The name of this GrokPattern.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this GrokPattern.
        The name key to tag this grok pattern.


        :param name: The name of this GrokPattern.
        :type: str
        """
        self._name = name

    @property
    def field_time_key(self):
        """
        Gets the field_time_key of this GrokPattern.
        Specify the time field for the event time. If the event doesn't have this field, the current time is used.


        :return: The field_time_key of this GrokPattern.
        :rtype: str
        """
        return self._field_time_key

    @field_time_key.setter
    def field_time_key(self, field_time_key):
        """
        Sets the field_time_key of this GrokPattern.
        Specify the time field for the event time. If the event doesn't have this field, the current time is used.


        :param field_time_key: The field_time_key of this GrokPattern.
        :type: str
        """
        self._field_time_key = field_time_key

    @property
    def field_time_format(self):
        """
        Gets the field_time_format of this GrokPattern.
        Process value using the specified format. This is available only when time_type is a string.


        :return: The field_time_format of this GrokPattern.
        :rtype: str
        """
        return self._field_time_format

    @field_time_format.setter
    def field_time_format(self, field_time_format):
        """
        Sets the field_time_format of this GrokPattern.
        Process value using the specified format. This is available only when time_type is a string.


        :param field_time_format: The field_time_format of this GrokPattern.
        :type: str
        """
        self._field_time_format = field_time_format

    @property
    def field_time_zone(self):
        """
        Gets the field_time_zone of this GrokPattern.
        Use the specified time zone. The time value can be parsed or formatted in the specified time zone.


        :return: The field_time_zone of this GrokPattern.
        :rtype: str
        """
        return self._field_time_zone

    @field_time_zone.setter
    def field_time_zone(self, field_time_zone):
        """
        Sets the field_time_zone of this GrokPattern.
        Use the specified time zone. The time value can be parsed or formatted in the specified time zone.


        :param field_time_zone: The field_time_zone of this GrokPattern.
        :type: str
        """
        self._field_time_zone = field_time_zone

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
