# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReportSummary(object):
    """
    The model of a single report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReportSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param report_type:
            The value to assign to the report_type property of this ReportSummary.
        :type report_type: str

        :param date:
            The value to assign to the date property of this ReportSummary.
        :type date: datetime

        :param columns:
            The value to assign to the columns property of this ReportSummary.
        :type columns: list[str]

        :param content:
            The value to assign to the content property of this ReportSummary.
        :type content: str

        """
        self.swagger_types = {
            'report_type': 'str',
            'date': 'datetime',
            'columns': 'list[str]',
            'content': 'str'
        }

        self.attribute_map = {
            'report_type': 'reportType',
            'date': 'date',
            'columns': 'columns',
            'content': 'content'
        }

        self._report_type = None
        self._date = None
        self._columns = None
        self._content = None

    @property
    def report_type(self):
        """
        **[Required]** Gets the report_type of this ReportSummary.
        The type of report.


        :return: The report_type of this ReportSummary.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """
        Sets the report_type of this ReportSummary.
        The type of report.


        :param report_type: The report_type of this ReportSummary.
        :type: str
        """
        self._report_type = report_type

    @property
    def date(self):
        """
        **[Required]** Gets the date of this ReportSummary.
        The date of the report.


        :return: The date of this ReportSummary.
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this ReportSummary.
        The date of the report.


        :param date: The date of this ReportSummary.
        :type: datetime
        """
        self._date = date

    @property
    def columns(self):
        """
        **[Required]** Gets the columns of this ReportSummary.
        The columns in the report.


        :return: The columns of this ReportSummary.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this ReportSummary.
        The columns in the report.


        :param columns: The columns of this ReportSummary.
        :type: list[str]
        """
        self._columns = columns

    @property
    def content(self):
        """
        **[Required]** Gets the content of this ReportSummary.
        The contents of the report in comma-separated values (CSV) file format.


        :return: The content of this ReportSummary.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """
        Sets the content of this ReportSummary.
        The contents of the report in comma-separated values (CSV) file format.


        :param content: The content of this ReportSummary.
        :type: str
        """
        self._content = content

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
