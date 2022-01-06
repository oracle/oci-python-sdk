# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MeasuredBootReport(object):
    """
    The measured boot report for a shielded instance.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MeasuredBootReport object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_policy_verification_successful:
            The value to assign to the is_policy_verification_successful property of this MeasuredBootReport.
        :type is_policy_verification_successful: bool

        :param measurements:
            The value to assign to the measurements property of this MeasuredBootReport.
        :type measurements: oci.core.models.MeasuredBootReportMeasurements

        """
        self.swagger_types = {
            'is_policy_verification_successful': 'bool',
            'measurements': 'MeasuredBootReportMeasurements'
        }

        self.attribute_map = {
            'is_policy_verification_successful': 'isPolicyVerificationSuccessful',
            'measurements': 'measurements'
        }

        self._is_policy_verification_successful = None
        self._measurements = None

    @property
    def is_policy_verification_successful(self):
        """
        **[Required]** Gets the is_policy_verification_successful of this MeasuredBootReport.
        Whether the verification succeeded, and the new values match the expected values.


        :return: The is_policy_verification_successful of this MeasuredBootReport.
        :rtype: bool
        """
        return self._is_policy_verification_successful

    @is_policy_verification_successful.setter
    def is_policy_verification_successful(self, is_policy_verification_successful):
        """
        Sets the is_policy_verification_successful of this MeasuredBootReport.
        Whether the verification succeeded, and the new values match the expected values.


        :param is_policy_verification_successful: The is_policy_verification_successful of this MeasuredBootReport.
        :type: bool
        """
        self._is_policy_verification_successful = is_policy_verification_successful

    @property
    def measurements(self):
        """
        Gets the measurements of this MeasuredBootReport.

        :return: The measurements of this MeasuredBootReport.
        :rtype: oci.core.models.MeasuredBootReportMeasurements
        """
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        """
        Sets the measurements of this MeasuredBootReport.

        :param measurements: The measurements of this MeasuredBootReport.
        :type: oci.core.models.MeasuredBootReportMeasurements
        """
        self._measurements = measurements

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
