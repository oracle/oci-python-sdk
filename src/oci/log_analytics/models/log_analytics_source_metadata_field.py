# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsSourceMetadataField(object):
    """
    LogAnalyticsSourceMetadataField
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsSourceMetadataField object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param field_name:
            The value to assign to the field_name property of this LogAnalyticsSourceMetadataField.
        :type field_name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this LogAnalyticsSourceMetadataField.
        :type is_enabled: bool

        :param is_system:
            The value to assign to the is_system property of this LogAnalyticsSourceMetadataField.
        :type is_system: bool

        :param key:
            The value to assign to the key property of this LogAnalyticsSourceMetadataField.
        :type key: str

        :param source_name:
            The value to assign to the source_name property of this LogAnalyticsSourceMetadataField.
        :type source_name: str

        """
        self.swagger_types = {
            'field_name': 'str',
            'is_enabled': 'bool',
            'is_system': 'bool',
            'key': 'str',
            'source_name': 'str'
        }

        self.attribute_map = {
            'field_name': 'fieldName',
            'is_enabled': 'isEnabled',
            'is_system': 'isSystem',
            'key': 'key',
            'source_name': 'sourceName'
        }

        self._field_name = None
        self._is_enabled = None
        self._is_system = None
        self._key = None
        self._source_name = None

    @property
    def field_name(self):
        """
        Gets the field_name of this LogAnalyticsSourceMetadataField.
        The field internal name.


        :return: The field_name of this LogAnalyticsSourceMetadataField.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """
        Sets the field_name of this LogAnalyticsSourceMetadataField.
        The field internal name.


        :param field_name: The field_name of this LogAnalyticsSourceMetadataField.
        :type: str
        """
        self._field_name = field_name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this LogAnalyticsSourceMetadataField.
        A flag inidcating whether or not the source metadata field is enabled.


        :return: The is_enabled of this LogAnalyticsSourceMetadataField.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this LogAnalyticsSourceMetadataField.
        A flag inidcating whether or not the source metadata field is enabled.


        :param is_enabled: The is_enabled of this LogAnalyticsSourceMetadataField.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def is_system(self):
        """
        Gets the is_system of this LogAnalyticsSourceMetadataField.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :return: The is_system of this LogAnalyticsSourceMetadataField.
        :rtype: bool
        """
        return self._is_system

    @is_system.setter
    def is_system(self, is_system):
        """
        Sets the is_system of this LogAnalyticsSourceMetadataField.
        The system flag.  A value of false denotes a custom, or user
        defined object.  A value of true denotes a built in object.


        :param is_system: The is_system of this LogAnalyticsSourceMetadataField.
        :type: bool
        """
        self._is_system = is_system

    @property
    def key(self):
        """
        Gets the key of this LogAnalyticsSourceMetadataField.
        The key.


        :return: The key of this LogAnalyticsSourceMetadataField.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this LogAnalyticsSourceMetadataField.
        The key.


        :param key: The key of this LogAnalyticsSourceMetadataField.
        :type: str
        """
        self._key = key

    @property
    def source_name(self):
        """
        Gets the source_name of this LogAnalyticsSourceMetadataField.
        The source internal name.


        :return: The source_name of this LogAnalyticsSourceMetadataField.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        """
        Sets the source_name of this LogAnalyticsSourceMetadataField.
        The source internal name.


        :param source_name: The source_name of this LogAnalyticsSourceMetadataField.
        :type: str
        """
        self._source_name = source_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
