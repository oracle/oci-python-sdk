# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_column_source_details import UpdateColumnSourceDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateColumnSourceTargetDetails(UpdateColumnSourceDetails):
    """
    Details of the target database to be associated as the column source with a masking policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateColumnSourceTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.data_safe.models.UpdateColumnSourceTargetDetails.column_source` attribute
        of this class is ``TARGET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param column_source:
            The value to assign to the column_source property of this UpdateColumnSourceTargetDetails.
            Allowed values for this property are: "TARGET", "SENSITIVE_DATA_MODEL"
        :type column_source: str

        :param target_id:
            The value to assign to the target_id property of this UpdateColumnSourceTargetDetails.
        :type target_id: str

        """
        self.swagger_types = {
            'column_source': 'str',
            'target_id': 'str'
        }

        self.attribute_map = {
            'column_source': 'columnSource',
            'target_id': 'targetId'
        }

        self._column_source = None
        self._target_id = None
        self._column_source = 'TARGET'

    @property
    def target_id(self):
        """
        **[Required]** Gets the target_id of this UpdateColumnSourceTargetDetails.
        The OCID of the target database to be associated as the column source with the masking policy.


        :return: The target_id of this UpdateColumnSourceTargetDetails.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this UpdateColumnSourceTargetDetails.
        The OCID of the target database to be associated as the column source with the masking policy.


        :param target_id: The target_id of this UpdateColumnSourceTargetDetails.
        :type: str
        """
        self._target_id = target_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
