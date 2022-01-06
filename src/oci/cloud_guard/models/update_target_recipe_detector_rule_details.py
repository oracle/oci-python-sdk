# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetRecipeDetectorRuleDetails(object):
    """
    The details to be updated in TargetDetectorRecipeDetectorRule
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetRecipeDetectorRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param detector_rule_id:
            The value to assign to the detector_rule_id property of this UpdateTargetRecipeDetectorRuleDetails.
        :type detector_rule_id: str

        :param details:
            The value to assign to the details property of this UpdateTargetRecipeDetectorRuleDetails.
        :type details: oci.cloud_guard.models.UpdateTargetDetectorRuleDetails

        """
        self.swagger_types = {
            'detector_rule_id': 'str',
            'details': 'UpdateTargetDetectorRuleDetails'
        }

        self.attribute_map = {
            'detector_rule_id': 'detectorRuleId',
            'details': 'details'
        }

        self._detector_rule_id = None
        self._details = None

    @property
    def detector_rule_id(self):
        """
        **[Required]** Gets the detector_rule_id of this UpdateTargetRecipeDetectorRuleDetails.
        Identifier for DetectorRule.


        :return: The detector_rule_id of this UpdateTargetRecipeDetectorRuleDetails.
        :rtype: str
        """
        return self._detector_rule_id

    @detector_rule_id.setter
    def detector_rule_id(self, detector_rule_id):
        """
        Sets the detector_rule_id of this UpdateTargetRecipeDetectorRuleDetails.
        Identifier for DetectorRule.


        :param detector_rule_id: The detector_rule_id of this UpdateTargetRecipeDetectorRuleDetails.
        :type: str
        """
        self._detector_rule_id = detector_rule_id

    @property
    def details(self):
        """
        **[Required]** Gets the details of this UpdateTargetRecipeDetectorRuleDetails.

        :return: The details of this UpdateTargetRecipeDetectorRuleDetails.
        :rtype: oci.cloud_guard.models.UpdateTargetDetectorRuleDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this UpdateTargetRecipeDetectorRuleDetails.

        :param details: The details of this UpdateTargetRecipeDetectorRuleDetails.
        :type: oci.cloud_guard.models.UpdateTargetDetectorRuleDetails
        """
        self._details = details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
