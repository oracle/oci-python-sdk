# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateReportDetails(object):
    """
    Details for the report generation.
    """

    #: A constant which can be used with the mime_type property of a GenerateReportDetails.
    #: This constant has a value of "PDF"
    MIME_TYPE_PDF = "PDF"

    #: A constant which can be used with the mime_type property of a GenerateReportDetails.
    #: This constant has a value of "XLS"
    MIME_TYPE_XLS = "XLS"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateReportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this GenerateReportDetails.
        :type display_name: str

        :param target_ids:
            The value to assign to the target_ids property of this GenerateReportDetails.
        :type target_ids: list[str]

        :param description:
            The value to assign to the description property of this GenerateReportDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GenerateReportDetails.
        :type compartment_id: str

        :param mime_type:
            The value to assign to the mime_type property of this GenerateReportDetails.
            Allowed values for this property are: "PDF", "XLS"
        :type mime_type: str

        :param time_less_than:
            The value to assign to the time_less_than property of this GenerateReportDetails.
        :type time_less_than: datetime

        :param time_greater_than:
            The value to assign to the time_greater_than property of this GenerateReportDetails.
        :type time_greater_than: datetime

        :param row_limit:
            The value to assign to the row_limit property of this GenerateReportDetails.
        :type row_limit: int

        """
        self.swagger_types = {
            'display_name': 'str',
            'target_ids': 'list[str]',
            'description': 'str',
            'compartment_id': 'str',
            'mime_type': 'str',
            'time_less_than': 'datetime',
            'time_greater_than': 'datetime',
            'row_limit': 'int'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'target_ids': 'targetIds',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'mime_type': 'mimeType',
            'time_less_than': 'timeLessThan',
            'time_greater_than': 'timeGreaterThan',
            'row_limit': 'rowLimit'
        }

        self._display_name = None
        self._target_ids = None
        self._description = None
        self._compartment_id = None
        self._mime_type = None
        self._time_less_than = None
        self._time_greater_than = None
        self._row_limit = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this GenerateReportDetails.
        The name of the report to be generated


        :return: The display_name of this GenerateReportDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this GenerateReportDetails.
        The name of the report to be generated


        :param display_name: The display_name of this GenerateReportDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def target_ids(self):
        """
        Gets the target_ids of this GenerateReportDetails.
        Array of database target OCIDs.


        :return: The target_ids of this GenerateReportDetails.
        :rtype: list[str]
        """
        return self._target_ids

    @target_ids.setter
    def target_ids(self, target_ids):
        """
        Sets the target_ids of this GenerateReportDetails.
        Array of database target OCIDs.


        :param target_ids: The target_ids of this GenerateReportDetails.
        :type: list[str]
        """
        self._target_ids = target_ids

    @property
    def description(self):
        """
        Gets the description of this GenerateReportDetails.
        The description of the report to be generated


        :return: The description of this GenerateReportDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GenerateReportDetails.
        The description of the report to be generated


        :param description: The description of this GenerateReportDetails.
        :type: str
        """
        self._description = description

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this GenerateReportDetails.
        The `OCID`__ of the compartment
        into which the resource should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this GenerateReportDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this GenerateReportDetails.
        The `OCID`__ of the compartment
        into which the resource should be moved.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this GenerateReportDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def mime_type(self):
        """
        **[Required]** Gets the mime_type of this GenerateReportDetails.
        Specifies the format of report to be excel or pdf

        Allowed values for this property are: "PDF", "XLS"


        :return: The mime_type of this GenerateReportDetails.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """
        Sets the mime_type of this GenerateReportDetails.
        Specifies the format of report to be excel or pdf


        :param mime_type: The mime_type of this GenerateReportDetails.
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
    def time_less_than(self):
        """
        Gets the time_less_than of this GenerateReportDetails.
        Specifies the time before which the data needs to be reported.


        :return: The time_less_than of this GenerateReportDetails.
        :rtype: datetime
        """
        return self._time_less_than

    @time_less_than.setter
    def time_less_than(self, time_less_than):
        """
        Sets the time_less_than of this GenerateReportDetails.
        Specifies the time before which the data needs to be reported.


        :param time_less_than: The time_less_than of this GenerateReportDetails.
        :type: datetime
        """
        self._time_less_than = time_less_than

    @property
    def time_greater_than(self):
        """
        Gets the time_greater_than of this GenerateReportDetails.
        Specifies the time after which the data needs to be reported.


        :return: The time_greater_than of this GenerateReportDetails.
        :rtype: datetime
        """
        return self._time_greater_than

    @time_greater_than.setter
    def time_greater_than(self, time_greater_than):
        """
        Sets the time_greater_than of this GenerateReportDetails.
        Specifies the time after which the data needs to be reported.


        :param time_greater_than: The time_greater_than of this GenerateReportDetails.
        :type: datetime
        """
        self._time_greater_than = time_greater_than

    @property
    def row_limit(self):
        """
        Gets the row_limit of this GenerateReportDetails.
        Specifies the limit on number of rows in report.


        :return: The row_limit of this GenerateReportDetails.
        :rtype: int
        """
        return self._row_limit

    @row_limit.setter
    def row_limit(self, row_limit):
        """
        Sets the row_limit of this GenerateReportDetails.
        Specifies the limit on number of rows in report.


        :param row_limit: The row_limit of this GenerateReportDetails.
        :type: int
        """
        self._row_limit = row_limit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
