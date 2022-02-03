# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryReportStatementCounts(object):
    """
    The number of statements in the SQL Tuning Advisor summary report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryReportStatementCounts object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param distinct_sql:
            The value to assign to the distinct_sql property of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type distinct_sql: int

        :param total_sql:
            The value to assign to the total_sql property of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type total_sql: int

        :param finding_count:
            The value to assign to the finding_count property of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type finding_count: int

        :param error_count:
            The value to assign to the error_count property of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type error_count: int

        """
        self.swagger_types = {
            'distinct_sql': 'int',
            'total_sql': 'int',
            'finding_count': 'int',
            'error_count': 'int'
        }

        self.attribute_map = {
            'distinct_sql': 'distinctSql',
            'total_sql': 'totalSql',
            'finding_count': 'findingCount',
            'error_count': 'errorCount'
        }

        self._distinct_sql = None
        self._total_sql = None
        self._finding_count = None
        self._error_count = None

    @property
    def distinct_sql(self):
        """
        **[Required]** Gets the distinct_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The number of distinct SQL statements.


        :return: The distinct_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :rtype: int
        """
        return self._distinct_sql

    @distinct_sql.setter
    def distinct_sql(self, distinct_sql):
        """
        Sets the distinct_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The number of distinct SQL statements.


        :param distinct_sql: The distinct_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type: int
        """
        self._distinct_sql = distinct_sql

    @property
    def total_sql(self):
        """
        **[Required]** Gets the total_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The total number of SQL statements.


        :return: The total_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :rtype: int
        """
        return self._total_sql

    @total_sql.setter
    def total_sql(self, total_sql):
        """
        Sets the total_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The total number of SQL statements.


        :param total_sql: The total_sql of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type: int
        """
        self._total_sql = total_sql

    @property
    def finding_count(self):
        """
        **[Required]** Gets the finding_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The number of distinct SQL statements with findings.


        :return: The finding_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :rtype: int
        """
        return self._finding_count

    @finding_count.setter
    def finding_count(self, finding_count):
        """
        Sets the finding_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The number of distinct SQL statements with findings.


        :param finding_count: The finding_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type: int
        """
        self._finding_count = finding_count

    @property
    def error_count(self):
        """
        **[Required]** Gets the error_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The number of distinct SQL statements with errors.


        :return: The error_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        """
        Sets the error_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        The number of distinct SQL statements with errors.


        :param error_count: The error_count of this SqlTuningAdvisorTaskSummaryReportStatementCounts.
        :type: int
        """
        self._error_count = error_count

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
