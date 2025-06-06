# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20201101


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SqlTuningAdvisorTaskSummaryReport(object):
    """
    The content of the SQL Tuning Advisor summary report.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SqlTuningAdvisorTaskSummaryReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param task_info:
            The value to assign to the task_info property of this SqlTuningAdvisorTaskSummaryReport.
        :type task_info: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportTaskInfo

        :param statistics:
            The value to assign to the statistics property of this SqlTuningAdvisorTaskSummaryReport.
        :type statistics: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportStatistics

        :param object_stat_findings:
            The value to assign to the object_stat_findings property of this SqlTuningAdvisorTaskSummaryReport.
        :type object_stat_findings: list[oci.database_management.models.SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary]

        :param index_findings:
            The value to assign to the index_findings property of this SqlTuningAdvisorTaskSummaryReport.
        :type index_findings: list[oci.database_management.models.SqlTuningAdvisorTaskSummaryReportIndexFindingSummary]

        """
        self.swagger_types = {
            'task_info': 'SqlTuningAdvisorTaskSummaryReportTaskInfo',
            'statistics': 'SqlTuningAdvisorTaskSummaryReportStatistics',
            'object_stat_findings': 'list[SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary]',
            'index_findings': 'list[SqlTuningAdvisorTaskSummaryReportIndexFindingSummary]'
        }
        self.attribute_map = {
            'task_info': 'taskInfo',
            'statistics': 'statistics',
            'object_stat_findings': 'objectStatFindings',
            'index_findings': 'indexFindings'
        }
        self._task_info = None
        self._statistics = None
        self._object_stat_findings = None
        self._index_findings = None

    @property
    def task_info(self):
        """
        **[Required]** Gets the task_info of this SqlTuningAdvisorTaskSummaryReport.

        :return: The task_info of this SqlTuningAdvisorTaskSummaryReport.
        :rtype: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportTaskInfo
        """
        return self._task_info

    @task_info.setter
    def task_info(self, task_info):
        """
        Sets the task_info of this SqlTuningAdvisorTaskSummaryReport.

        :param task_info: The task_info of this SqlTuningAdvisorTaskSummaryReport.
        :type: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportTaskInfo
        """
        self._task_info = task_info

    @property
    def statistics(self):
        """
        **[Required]** Gets the statistics of this SqlTuningAdvisorTaskSummaryReport.

        :return: The statistics of this SqlTuningAdvisorTaskSummaryReport.
        :rtype: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """
        Sets the statistics of this SqlTuningAdvisorTaskSummaryReport.

        :param statistics: The statistics of this SqlTuningAdvisorTaskSummaryReport.
        :type: oci.database_management.models.SqlTuningAdvisorTaskSummaryReportStatistics
        """
        self._statistics = statistics

    @property
    def object_stat_findings(self):
        """
        Gets the object_stat_findings of this SqlTuningAdvisorTaskSummaryReport.
        The list of object findings related to statistics.


        :return: The object_stat_findings of this SqlTuningAdvisorTaskSummaryReport.
        :rtype: list[oci.database_management.models.SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary]
        """
        return self._object_stat_findings

    @object_stat_findings.setter
    def object_stat_findings(self, object_stat_findings):
        """
        Sets the object_stat_findings of this SqlTuningAdvisorTaskSummaryReport.
        The list of object findings related to statistics.


        :param object_stat_findings: The object_stat_findings of this SqlTuningAdvisorTaskSummaryReport.
        :type: list[oci.database_management.models.SqlTuningAdvisorTaskSummaryReportObjectStatFindingSummary]
        """
        self._object_stat_findings = object_stat_findings

    @property
    def index_findings(self):
        """
        Gets the index_findings of this SqlTuningAdvisorTaskSummaryReport.
        The list of object findings related to indexes.


        :return: The index_findings of this SqlTuningAdvisorTaskSummaryReport.
        :rtype: list[oci.database_management.models.SqlTuningAdvisorTaskSummaryReportIndexFindingSummary]
        """
        return self._index_findings

    @index_findings.setter
    def index_findings(self, index_findings):
        """
        Sets the index_findings of this SqlTuningAdvisorTaskSummaryReport.
        The list of object findings related to indexes.


        :param index_findings: The index_findings of this SqlTuningAdvisorTaskSummaryReport.
        :type: list[oci.database_management.models.SqlTuningAdvisorTaskSummaryReportIndexFindingSummary]
        """
        self._index_findings = index_findings

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
