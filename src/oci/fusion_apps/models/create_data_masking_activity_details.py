# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataMaskingActivityDetails(object):
    """
    The information about current data masking request.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataMaskingActivityDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param is_resume_data_masking:
            The value to assign to the is_resume_data_masking property of this CreateDataMaskingActivityDetails.
        :type is_resume_data_masking: bool

        """
        self.swagger_types = {
            'is_resume_data_masking': 'bool'
        }

        self.attribute_map = {
            'is_resume_data_masking': 'isResumeDataMasking'
        }

        self._is_resume_data_masking = None

    @property
    def is_resume_data_masking(self):
        """
        Gets the is_resume_data_masking of this CreateDataMaskingActivityDetails.
        This allows the Data Safe service to resume the previously failed data masking activity.


        :return: The is_resume_data_masking of this CreateDataMaskingActivityDetails.
        :rtype: bool
        """
        return self._is_resume_data_masking

    @is_resume_data_masking.setter
    def is_resume_data_masking(self, is_resume_data_masking):
        """
        Sets the is_resume_data_masking of this CreateDataMaskingActivityDetails.
        This allows the Data Safe service to resume the previously failed data masking activity.


        :param is_resume_data_masking: The is_resume_data_masking of this CreateDataMaskingActivityDetails.
        :type: bool
        """
        self._is_resume_data_masking = is_resume_data_masking

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
