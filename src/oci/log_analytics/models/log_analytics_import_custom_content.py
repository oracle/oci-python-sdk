# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class LogAnalyticsImportCustomContent(object):
    """
    LogAnalyticsImportCustomContent
    """

    def __init__(self, **kwargs):
        """
        Initializes a new LogAnalyticsImportCustomContent object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param parser_names:
            The value to assign to the parser_names property of this LogAnalyticsImportCustomContent.
        :type parser_names: list[str]

        :param source_names:
            The value to assign to the source_names property of this LogAnalyticsImportCustomContent.
        :type source_names: list[str]

        :param field_names:
            The value to assign to the field_names property of this LogAnalyticsImportCustomContent.
        :type field_names: list[str]

        :param change_list:
            The value to assign to the change_list property of this LogAnalyticsImportCustomContent.
        :type change_list: oci.log_analytics.models.LogAnalyticsImportCustomChangeList

        :param content_name:
            The value to assign to the content_name property of this LogAnalyticsImportCustomContent.
        :type content_name: str

        """
        self.swagger_types = {
            'parser_names': 'list[str]',
            'source_names': 'list[str]',
            'field_names': 'list[str]',
            'change_list': 'LogAnalyticsImportCustomChangeList',
            'content_name': 'str'
        }

        self.attribute_map = {
            'parser_names': 'parserNames',
            'source_names': 'sourceNames',
            'field_names': 'fieldNames',
            'change_list': 'changeList',
            'content_name': 'contentName'
        }

        self._parser_names = None
        self._source_names = None
        self._field_names = None
        self._change_list = None
        self._content_name = None

    @property
    def parser_names(self):
        """
        Gets the parser_names of this LogAnalyticsImportCustomContent.
        The parser names.


        :return: The parser_names of this LogAnalyticsImportCustomContent.
        :rtype: list[str]
        """
        return self._parser_names

    @parser_names.setter
    def parser_names(self, parser_names):
        """
        Sets the parser_names of this LogAnalyticsImportCustomContent.
        The parser names.


        :param parser_names: The parser_names of this LogAnalyticsImportCustomContent.
        :type: list[str]
        """
        self._parser_names = parser_names

    @property
    def source_names(self):
        """
        Gets the source_names of this LogAnalyticsImportCustomContent.
        The source names.


        :return: The source_names of this LogAnalyticsImportCustomContent.
        :rtype: list[str]
        """
        return self._source_names

    @source_names.setter
    def source_names(self, source_names):
        """
        Sets the source_names of this LogAnalyticsImportCustomContent.
        The source names.


        :param source_names: The source_names of this LogAnalyticsImportCustomContent.
        :type: list[str]
        """
        self._source_names = source_names

    @property
    def field_names(self):
        """
        Gets the field_names of this LogAnalyticsImportCustomContent.
        The field names.


        :return: The field_names of this LogAnalyticsImportCustomContent.
        :rtype: list[str]
        """
        return self._field_names

    @field_names.setter
    def field_names(self, field_names):
        """
        Sets the field_names of this LogAnalyticsImportCustomContent.
        The field names.


        :param field_names: The field_names of this LogAnalyticsImportCustomContent.
        :type: list[str]
        """
        self._field_names = field_names

    @property
    def change_list(self):
        """
        Gets the change_list of this LogAnalyticsImportCustomContent.

        :return: The change_list of this LogAnalyticsImportCustomContent.
        :rtype: oci.log_analytics.models.LogAnalyticsImportCustomChangeList
        """
        return self._change_list

    @change_list.setter
    def change_list(self, change_list):
        """
        Sets the change_list of this LogAnalyticsImportCustomContent.

        :param change_list: The change_list of this LogAnalyticsImportCustomContent.
        :type: oci.log_analytics.models.LogAnalyticsImportCustomChangeList
        """
        self._change_list = change_list

    @property
    def content_name(self):
        """
        Gets the content_name of this LogAnalyticsImportCustomContent.
        The content name.


        :return: The content_name of this LogAnalyticsImportCustomContent.
        :rtype: str
        """
        return self._content_name

    @content_name.setter
    def content_name(self, content_name):
        """
        Sets the content_name of this LogAnalyticsImportCustomContent.
        The content name.


        :param content_name: The content_name of this LogAnalyticsImportCustomContent.
        :type: str
        """
        self._content_name = content_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
