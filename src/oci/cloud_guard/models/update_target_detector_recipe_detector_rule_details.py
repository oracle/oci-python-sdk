# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200131


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTargetDetectorRecipeDetectorRuleDetails(object):
    """
    Parameters to use to update a detector rule in a detector recipe attached to a target.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTargetDetectorRecipeDetectorRuleDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param details:
            The value to assign to the details property of this UpdateTargetDetectorRecipeDetectorRuleDetails.
        :type details: oci.cloud_guard.models.UpdateTargetDetectorRuleDetails

        """
        self.swagger_types = {
            'details': 'UpdateTargetDetectorRuleDetails'
        }
        self.attribute_map = {
            'details': 'details'
        }
        self._details = None

    @property
    def details(self):
        """
        **[Required]** Gets the details of this UpdateTargetDetectorRecipeDetectorRuleDetails.

        :return: The details of this UpdateTargetDetectorRecipeDetectorRuleDetails.
        :rtype: oci.cloud_guard.models.UpdateTargetDetectorRuleDetails
        """
        return self._details

    @details.setter
    def details(self, details):
        """
        Sets the details of this UpdateTargetDetectorRecipeDetectorRuleDetails.

        :param details: The details of this UpdateTargetDetectorRecipeDetectorRuleDetails.
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
