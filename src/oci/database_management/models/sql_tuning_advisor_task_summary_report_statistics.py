# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryReportStatistics(object):
    """
    The statistics of the statements and findings in the SQL Tuning Advisor summary report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryReportStatistics object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param statement_counts:
            The value to assign to the statement_counts property of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :type statement_counts: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportStatementCounts

        :param finding_counts:
            The value to assign to the finding_counts property of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :type finding_counts: oci.database_management.models.SqlTuningAdvisorTaskSummaryFindingCounts

        :param finding_benefits:
            The value to assign to the finding_benefits property of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :type finding_benefits: oci.database_management.models.SqlTuningAdvisorTaskSummaryFindingBenefits

        """
        self.swagger_types = {
            'statement_counts': 'SqlTuningAdvisorTaskSummaryReportStatementCounts',
            'finding_counts': 'SqlTuningAdvisorTaskSummaryFindingCounts',
            'finding_benefits': 'SqlTuningAdvisorTaskSummaryFindingBenefits'
        }

        self.attribute_map = {
            'statement_counts': 'statementCounts',
            'finding_counts': 'findingCounts',
            'finding_benefits': 'findingBenefits'
        }

        self._statement_counts = None
        self._finding_counts = None
        self._finding_benefits = None

    @property
    def statement_counts(self):
        """
        **[Required]** Gets the statement_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.

        :return: The statement_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :rtype: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportStatementCounts
        """
        return self._statement_counts

    @statement_counts.setter
    def statement_counts(self, statement_counts):
        """
        Sets the statement_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.

        :param statement_counts: The statement_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :type: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportStatementCounts
        """
        self._statement_counts = statement_counts

    @property
    def finding_counts(self):
        """
        **[Required]** Gets the finding_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.

        :return: The finding_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :rtype: oci.database_management.models.SqlTuningAdvisorTaskSummaryFindingCounts
        """
        return self._finding_counts

    @finding_counts.setter
    def finding_counts(self, finding_counts):
        """
        Sets the finding_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.

        :param finding_counts: The finding_counts of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :type: oci.database_management.models.SqlTuningAdvisorTaskSummaryFindingCounts
        """
        self._finding_counts = finding_counts

    @property
    def finding_benefits(self):
        """
        **[Required]** Gets the finding_benefits of this SqlTuningAdvisorTaskSummaryReportStatistics.

        :return: The finding_benefits of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :rtype: oci.database_management.models.SqlTuningAdvisorTaskSummaryFindingBenefits
        """
        return self._finding_benefits

    @finding_benefits.setter
    def finding_benefits(self, finding_benefits):
        """
        Sets the finding_benefits of this SqlTuningAdvisorTaskSummaryReportStatistics.

        :param finding_benefits: The finding_benefits of this SqlTuningAdvisorTaskSummaryReportStatistics.
        :type: oci.database_management.models.SqlTuningAdvisorTaskSummaryFindingBenefits
        """
        self._finding_benefits = finding_benefits

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
