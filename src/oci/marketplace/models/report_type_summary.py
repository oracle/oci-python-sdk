# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReportTypeSummary(object):
    """
    The model of the description of a report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ReportTypeSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param report_type:
            The value to assign to the report_type property of this ReportTypeSummary.
        :type report_type: str

        :param name:
            The value to assign to the name property of this ReportTypeSummary.
        :type name: str

        :param description:
            The value to assign to the description property of this ReportTypeSummary.
        :type description: str

        :param columns:
            The value to assign to the columns property of this ReportTypeSummary.
        :type columns: list[str]

        """
        self.swagger_types = {
            'report_type': 'str',
            'name': 'str',
            'description': 'str',
            'columns': 'list[str]'
        }

        self.attribute_map = {
            'report_type': 'reportType',
            'name': 'name',
            'description': 'description',
            'columns': 'columns'
        }

        self._report_type = None
        self._name = None
        self._description = None
        self._columns = None

    @property
    def report_type(self):
        """
        Gets the report_type of this ReportTypeSummary.
        The type of report.


        :return: The report_type of this ReportTypeSummary.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """
        Sets the report_type of this ReportTypeSummary.
        The type of report.


        :param report_type: The report_type of this ReportTypeSummary.
        :type: str
        """
        self._report_type = report_type

    @property
    def name(self):
        """
        Gets the name of this ReportTypeSummary.
        The name of the report.


        :return: The name of this ReportTypeSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ReportTypeSummary.
        The name of the report.


        :param name: The name of this ReportTypeSummary.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ReportTypeSummary.
        A description of the report.


        :return: The description of this ReportTypeSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ReportTypeSummary.
        A description of the report.


        :param description: The description of this ReportTypeSummary.
        :type: str
        """
        self._description = description

    @property
    def columns(self):
        """
        Gets the columns of this ReportTypeSummary.
        The columns in the report.


        :return: The columns of this ReportTypeSummary.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """
        Sets the columns of this ReportTypeSummary.
        The columns in the report.


        :param columns: The columns of this ReportTypeSummary.
        :type: list[str]
        """
        self._columns = columns

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
