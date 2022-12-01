# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ReportDetails(object):
    """
    Details for the report schedule.
    """

    #: A constant which can be used with the report_type property of a ReportDetails.
    #: This constant has a value of "AUDIT"
    REPORT_TYPE_AUDIT = "AUDIT"

    def __init__(self, **kwargs):
        """
        Initializes a new ReportDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.ScheduleAuditReportDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param report_type:
            The value to assign to the report_type property of this ReportDetails.
            Allowed values for this property are: "AUDIT"
        :type report_type: str

        """
        self.swagger_types = {
            'report_type': 'str'
        }

        self.attribute_map = {
            'report_type': 'reportType'
        }

        self._report_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['reportType']

        if type == 'AUDIT':
            return 'ScheduleAuditReportDetails'
        else:
            return 'ReportDetails'

    @property
    def report_type(self):
        """
        **[Required]** Gets the report_type of this ReportDetails.
        Allowed values for this property are: "AUDIT"


        :return: The report_type of this ReportDetails.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """
        Sets the report_type of this ReportDetails.

        :param report_type: The report_type of this ReportDetails.
        :type: str
        """
        allowed_values = ["AUDIT"]
        if not value_allowed_none_or_none_sentinel(report_type, allowed_values):
            raise ValueError(
                "Invalid value for `report_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._report_type = report_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
