# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AwrReport(object):
    """
    The result of the AWR report.
    """

    #: A constant which can be used with the format property of a AwrReport.
    #: This constant has a value of "HTML"
    FORMAT_HTML = "HTML"

    #: A constant which can be used with the format property of a AwrReport.
    #: This constant has a value of "TEXT"
    FORMAT_TEXT = "TEXT"

    def __init__(self, **kwargs):
        """
        Initializes a new AwrReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param content:
            The value to assign to the content property of this AwrReport.
        :type content: str

        :param format:
            The value to assign to the format property of this AwrReport.
            Allowed values for this property are: "HTML", "TEXT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type format: str

        """
        self.swagger_types = {
            'content': 'str',
            'format': 'str'
        }

        self.attribute_map = {
            'content': 'content',
            'format': 'format'
        }

        self._content = None
        self._format = None

    @property
    def content(self):
        """
        Gets the content of this AwrReport.
        The content of the report.


        :return: The content of this AwrReport.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this AwrReport.
        The content of the report.


        :param content: The content of this AwrReport.
        :type: str
        """
        self._content = content

    @property
    def format(self):
        """
        **[Required]** Gets the format of this AwrReport.
        The format of the report.

        Allowed values for this property are: "HTML", "TEXT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The format of this AwrReport.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this AwrReport.
        The format of the report.


        :param format: The format of this AwrReport.
        :type: str
        """
        allowed_values = ["HTML", "TEXT"]
        if not value_allowed_none_or_none_sentinel(format, allowed_values):
            format = 'UNKNOWN_ENUM_VALUE'
        self._format = format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
