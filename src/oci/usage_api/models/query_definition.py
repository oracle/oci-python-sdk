# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QueryDefinition(object):
    """
    The common fields for queries.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new QueryDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this QueryDefinition.
        :type display_name: str

        :param report_query:
            The value to assign to the report_query property of this QueryDefinition.
        :type report_query: oci.usage_api.models.ReportQuery

        :param cost_analysis_ui:
            The value to assign to the cost_analysis_ui property of this QueryDefinition.
        :type cost_analysis_ui: oci.usage_api.models.CostAnalysisUI

        :param version:
            The value to assign to the version property of this QueryDefinition.
        :type version: float

        """
        self.swagger_types = {
            'display_name': 'str',
            'report_query': 'ReportQuery',
            'cost_analysis_ui': 'CostAnalysisUI',
            'version': 'float'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'report_query': 'reportQuery',
            'cost_analysis_ui': 'costAnalysisUI',
            'version': 'version'
        }

        self._display_name = None
        self._report_query = None
        self._cost_analysis_ui = None
        self._version = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this QueryDefinition.
        The query display name. Avoid entering confidential information.


        :return: The display_name of this QueryDefinition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this QueryDefinition.
        The query display name. Avoid entering confidential information.


        :param display_name: The display_name of this QueryDefinition.
        :type: str
        """
        self._display_name = display_name

    @property
    def report_query(self):
        """
        **[Required]** Gets the report_query of this QueryDefinition.

        :return: The report_query of this QueryDefinition.
        :rtype: oci.usage_api.models.ReportQuery
        """
        return self._report_query

    @report_query.setter
    def report_query(self, report_query):
        """
        Sets the report_query of this QueryDefinition.

        :param report_query: The report_query of this QueryDefinition.
        :type: oci.usage_api.models.ReportQuery
        """
        self._report_query = report_query

    @property
    def cost_analysis_ui(self):
        """
        **[Required]** Gets the cost_analysis_ui of this QueryDefinition.

        :return: The cost_analysis_ui of this QueryDefinition.
        :rtype: oci.usage_api.models.CostAnalysisUI
        """
        return self._cost_analysis_ui

    @cost_analysis_ui.setter
    def cost_analysis_ui(self, cost_analysis_ui):
        """
        Sets the cost_analysis_ui of this QueryDefinition.

        :param cost_analysis_ui: The cost_analysis_ui of this QueryDefinition.
        :type: oci.usage_api.models.CostAnalysisUI
        """
        self._cost_analysis_ui = cost_analysis_ui

    @property
    def version(self):
        """
        **[Required]** Gets the version of this QueryDefinition.
        the version of saved query.


        :return: The version of this QueryDefinition.
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """
        Sets the version of this QueryDefinition.
        the version of saved query.


        :param version: The version of this QueryDefinition.
        :type: float
        """
        self._version = version

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
