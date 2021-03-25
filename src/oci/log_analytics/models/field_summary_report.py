# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FieldSummaryReport(object):
    """
    FieldSummaryReport
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FieldSummaryReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param non_oob_count:
            The value to assign to the non_oob_count property of this FieldSummaryReport.
        :type non_oob_count: int

        :param oob_count:
            The value to assign to the oob_count property of this FieldSummaryReport.
        :type oob_count: int

        :param usage_details:
            The value to assign to the usage_details property of this FieldSummaryReport.
        :type usage_details: list[oci.log_analytics.models.UsageStatusItem]

        """
        self.swagger_types = {
            'non_oob_count': 'int',
            'oob_count': 'int',
            'usage_details': 'list[UsageStatusItem]'
        }

        self.attribute_map = {
            'non_oob_count': 'nonOobCount',
            'oob_count': 'oobCount',
            'usage_details': 'usageDetails'
        }

        self._non_oob_count = None
        self._oob_count = None
        self._usage_details = None

    @property
    def non_oob_count(self):
        """
        Gets the non_oob_count of this FieldSummaryReport.
        The count of custom (user defined) fields.


        :return: The non_oob_count of this FieldSummaryReport.
        :rtype: int
        """
        return self._non_oob_count

    @non_oob_count.setter
    def non_oob_count(self, non_oob_count):
        """
        Sets the non_oob_count of this FieldSummaryReport.
        The count of custom (user defined) fields.


        :param non_oob_count: The non_oob_count of this FieldSummaryReport.
        :type: int
        """
        self._non_oob_count = non_oob_count

    @property
    def oob_count(self):
        """
        Gets the oob_count of this FieldSummaryReport.
        The count of built in fields.


        :return: The oob_count of this FieldSummaryReport.
        :rtype: int
        """
        return self._oob_count

    @oob_count.setter
    def oob_count(self, oob_count):
        """
        Sets the oob_count of this FieldSummaryReport.
        The count of built in fields.


        :param oob_count: The oob_count of this FieldSummaryReport.
        :type: int
        """
        self._oob_count = oob_count

    @property
    def usage_details(self):
        """
        Gets the usage_details of this FieldSummaryReport.
        Field usage detailss


        :return: The usage_details of this FieldSummaryReport.
        :rtype: list[oci.log_analytics.models.UsageStatusItem]
        """
        return self._usage_details

    @usage_details.setter
    def usage_details(self, usage_details):
        """
        Sets the usage_details of this FieldSummaryReport.
        Field usage detailss


        :param usage_details: The usage_details of this FieldSummaryReport.
        :type: list[oci.log_analytics.models.UsageStatusItem]
        """
        self._usage_details = usage_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
