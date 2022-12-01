# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleReportDetails(object):
    """
    Details for the report schedule.
    """

    #: A constant which can be used with the mime_type property of a ScheduleReportDetails.
    #: This constant has a value of "PDF"
    MIME_TYPE_PDF = "PDF"

    #: A constant which can be used with the mime_type property of a ScheduleReportDetails.
    #: This constant has a value of "XLS"
    MIME_TYPE_XLS = "XLS"

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleReportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this ScheduleReportDetails.
        :type display_name: str

        :param schedule:
            The value to assign to the schedule property of this ScheduleReportDetails.
        :type schedule: str

        :param mime_type:
            The value to assign to the mime_type property of this ScheduleReportDetails.
            Allowed values for this property are: "PDF", "XLS"
        :type mime_type: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ScheduleReportDetails.
        :type compartment_id: str

        :param report_details:
            The value to assign to the report_details property of this ScheduleReportDetails.
        :type report_details: oci.data_safe.models.ReportDetails

        """
        self.swagger_types = {
            'display_name': 'str',
            'schedule': 'str',
            'mime_type': 'str',
            'compartment_id': 'str',
            'report_details': 'ReportDetails'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'schedule': 'schedule',
            'mime_type': 'mimeType',
            'compartment_id': 'compartmentId',
            'report_details': 'reportDetails'
        }

        self._display_name = None
        self._schedule = None
        self._mime_type = None
        self._compartment_id = None
        self._report_details = None

    @property
    def display_name(self):
        """
        Gets the display_name of this ScheduleReportDetails.
        The name of the report to be scheduled


        :return: The display_name of this ScheduleReportDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ScheduleReportDetails.
        The name of the report to be scheduled


        :param display_name: The display_name of this ScheduleReportDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def schedule(self):
        """
        **[Required]** Gets the schedule of this ScheduleReportDetails.
        Schedule to generate the report periodically in the specified format:
        <version-string>;<version-specific-schedule>

        Allowed version strings - \"v1\"
        v1's version specific schedule -<ss> <mm> <hh> <day-of-week> <day-of-month>
        Each of the above fields potentially introduce constraints. A workrequest is created only
        when clock time satisfies all the constraints. Constraints introduced:
        1. seconds = <ss> (So, the allowed range for <ss> is [0, 59])
        2. minutes = <mm> (So, the allowed range for <mm> is [0, 59])
        3. hours = <hh> (So, the allowed range for <hh> is [0, 23])
        4. <day-of-week> can be either '*' (without quotes or a number between 1(Monday) and 7(Sunday))
        No constraint introduced when it is '*'. When not, day of week must equal the given value
        5. <day-of-month> can be either '*' (without quotes or a number between 1 and 28)
        No constraint introduced when it is '*'. When not, day of month must equal the given value


        :return: The schedule of this ScheduleReportDetails.
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """
        Sets the schedule of this ScheduleReportDetails.
        Schedule to generate the report periodically in the specified format:
        <version-string>;<version-specific-schedule>

        Allowed version strings - \"v1\"
        v1's version specific schedule -<ss> <mm> <hh> <day-of-week> <day-of-month>
        Each of the above fields potentially introduce constraints. A workrequest is created only
        when clock time satisfies all the constraints. Constraints introduced:
        1. seconds = <ss> (So, the allowed range for <ss> is [0, 59])
        2. minutes = <mm> (So, the allowed range for <mm> is [0, 59])
        3. hours = <hh> (So, the allowed range for <hh> is [0, 23])
        4. <day-of-week> can be either '*' (without quotes or a number between 1(Monday) and 7(Sunday))
        No constraint introduced when it is '*'. When not, day of week must equal the given value
        5. <day-of-month> can be either '*' (without quotes or a number between 1 and 28)
        No constraint introduced when it is '*'. When not, day of month must equal the given value


        :param schedule: The schedule of this ScheduleReportDetails.
        :type: str
        """
        self._schedule = schedule

    @property
    def mime_type(self):
        """
        **[Required]** Gets the mime_type of this ScheduleReportDetails.
        Specifies the format of report to be excel or pdf

        Allowed values for this property are: "PDF", "XLS"


        :return: The mime_type of this ScheduleReportDetails.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this ScheduleReportDetails.
        Specifies the format of report to be excel or pdf


        :param mime_type: The mime_type of this ScheduleReportDetails.
        :type: str
        """
        allowed_values = ["PDF", "XLS"]
        if not value_allowed_none_or_none_sentinel(mime_type, allowed_values):
            raise ValueError(
                "Invalid value for `mime_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._mime_type = mime_type

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ScheduleReportDetails.
        The `OCID`__ of the compartment
        in which the resource should be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ScheduleReportDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ScheduleReportDetails.
        The `OCID`__ of the compartment
        in which the resource should be created.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ScheduleReportDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def report_details(self):
        """
        **[Required]** Gets the report_details of this ScheduleReportDetails.

        :return: The report_details of this ScheduleReportDetails.
        :rtype: oci.data_safe.models.ReportDetails
        """
        return self._report_details

    @report_details.setter
    def report_details(self, report_details):
        """
        Sets the report_details of this ScheduleReportDetails.

        :param report_details: The report_details of this ScheduleReportDetails.
        :type: oci.data_safe.models.ReportDetails
        """
        self._report_details = report_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
