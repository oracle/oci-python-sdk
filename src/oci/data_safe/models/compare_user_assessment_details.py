# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CompareUserAssessmentDetails(object):
    """
    The details of the user assessment comparison.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CompareUserAssessmentDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param comparison_user_assessment_id:
            The value to assign to the comparison_user_assessment_id property of this CompareUserAssessmentDetails.
        :type comparison_user_assessment_id: str

        """
        self.swagger_types = {
            'comparison_user_assessment_id': 'str'
        }

        self.attribute_map = {
            'comparison_user_assessment_id': 'comparisonUserAssessmentId'
        }

        self._comparison_user_assessment_id = None

    @property
    def comparison_user_assessment_id(self):
        """
        **[Required]** Gets the comparison_user_assessment_id of this CompareUserAssessmentDetails.
        The OCID of the user assessment to be compared. You can compare with another user assessment, a latest assessment, or a baseline.


        :return: The comparison_user_assessment_id of this CompareUserAssessmentDetails.
        :rtype: str
        """
        return self._comparison_user_assessment_id

    @comparison_user_assessment_id.setter
    def comparison_user_assessment_id(self, comparison_user_assessment_id):
        """
        Sets the comparison_user_assessment_id of this CompareUserAssessmentDetails.
        The OCID of the user assessment to be compared. You can compare with another user assessment, a latest assessment, or a baseline.


        :param comparison_user_assessment_id: The comparison_user_assessment_id of this CompareUserAssessmentDetails.
        :type: str
        """
        self._comparison_user_assessment_id = comparison_user_assessment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
