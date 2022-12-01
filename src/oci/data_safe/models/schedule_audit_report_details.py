# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .report_details import ReportDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleAuditReportDetails(ReportDetails):
    """
    Details for the audit report schedule.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleAuditReportDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.ScheduleAuditReportDetails.report_type` attribute
        of this class is ``AUDIT`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param report_type:
            The value to assign to the report_type property of this ScheduleAuditReportDetails.
            Allowed values for this property are: "AUDIT"
        :type report_type: str

        :param row_limit:
            The value to assign to the row_limit property of this ScheduleAuditReportDetails.
        :type row_limit: int

        :param record_time_span:
            The value to assign to the record_time_span property of this ScheduleAuditReportDetails.
        :type record_time_span: str

        """
        self.swagger_types = {
            'report_type': 'str',
            'row_limit': 'int',
            'record_time_span': 'str'
        }

        self.attribute_map = {
            'report_type': 'reportType',
            'row_limit': 'rowLimit',
            'record_time_span': 'recordTimeSpan'
        }

        self._report_type = None
        self._row_limit = None
        self._record_time_span = None
        self._report_type = 'AUDIT'

    @property
    def row_limit(self):
        """
        Gets the row_limit of this ScheduleAuditReportDetails.
        Specifies the limit on number of rows in report.


        :return: The row_limit of this ScheduleAuditReportDetails.
        :rtype: int
        """
        return self._row_limit

    @row_limit.setter
    def row_limit(self, row_limit):
        """
        Sets the row_limit of this ScheduleAuditReportDetails.
        Specifies the limit on number of rows in report.


        :param row_limit: The row_limit of this ScheduleAuditReportDetails.
        :type: int
        """
        self._row_limit = row_limit

    @property
    def record_time_span(self):
        """
        **[Required]** Gets the record_time_span of this ScheduleAuditReportDetails.
        The time span of records in report to be scheduled.
        <period-value><period>
        Allowed period strings - \"H\",\"D\",\"M\",\"Y\"
        Each of the above fields potentially introduce constraints. A workRequest is created only
        when period-value satisfies all the constraints. Constraints introduced:
        1. period = H (The allowed range for period-value is [1, 23])
        2. period = D (The allowed range for period-value is [1, 30])
        3. period = M (The allowed range for period-value is [1, 11])
        4. period = Y (The minimum period-value is 1)


        :return: The record_time_span of this ScheduleAuditReportDetails.
        :rtype: str
        """
        return self._record_time_span

    @record_time_span.setter
    def record_time_span(self, record_time_span):
        """
        Sets the record_time_span of this ScheduleAuditReportDetails.
        The time span of records in report to be scheduled.
        <period-value><period>
        Allowed period strings - \"H\",\"D\",\"M\",\"Y\"
        Each of the above fields potentially introduce constraints. A workRequest is created only
        when period-value satisfies all the constraints. Constraints introduced:
        1. period = H (The allowed range for period-value is [1, 23])
        2. period = D (The allowed range for period-value is [1, 30])
        3. period = M (The allowed range for period-value is [1, 11])
        4. period = Y (The minimum period-value is 1)


        :param record_time_span: The record_time_span of this ScheduleAuditReportDetails.
        :type: str
        """
        self._record_time_span = record_time_span

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
