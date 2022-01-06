# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GenerateSecurityAssessmentReportDetails(object):
    """
    The details used to generate a new security assessment report.
    """

    #: A constant which can be used with the format property of a GenerateSecurityAssessmentReportDetails.
    #: This constant has a value of "PDF"
    FORMAT_PDF = "PDF"

    #: A constant which can be used with the format property of a GenerateSecurityAssessmentReportDetails.
    #: This constant has a value of "XLS"
    FORMAT_XLS = "XLS"

    def __init__(self, **kwargs):
        """
        Initializes a new GenerateSecurityAssessmentReportDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param format:
            The value to assign to the format property of this GenerateSecurityAssessmentReportDetails.
            Allowed values for this property are: "PDF", "XLS"
        :type format: str

        """
        self.swagger_types = {
            'format': 'str'
        }

        self.attribute_map = {
            'format': 'format'
        }

        self._format = None

    @property
    def format(self):
        """
        **[Required]** Gets the format of this GenerateSecurityAssessmentReportDetails.
        Format of the report.

        Allowed values for this property are: "PDF", "XLS"


        :return: The format of this GenerateSecurityAssessmentReportDetails.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """
        Sets the format of this GenerateSecurityAssessmentReportDetails.
        Format of the report.


        :param format: The format of this GenerateSecurityAssessmentReportDetails.
        :type: str
        """
        allowed_values = ["PDF", "XLS"]
        if not value_allowed_none_or_none_sentinel(format, allowed_values):
            raise ValueError(
                "Invalid value for `format`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._format = format

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
