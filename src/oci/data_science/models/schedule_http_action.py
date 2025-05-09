# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20190101

from .schedule_action import ScheduleAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ScheduleHttpAction(ScheduleAction):
    """
    this is HTTP action
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ScheduleHttpAction object with values from keyword arguments. The default value of the :py:attr:`~oci.data_science.models.ScheduleHttpAction.action_type` attribute
        of this class is ``HTTP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action_type:
            The value to assign to the action_type property of this ScheduleHttpAction.
            Allowed values for this property are: "HTTP"
        :type action_type: str

        :param action_details:
            The value to assign to the action_details property of this ScheduleHttpAction.
        :type action_details: oci.data_science.models.ScheduleHttpActionDetails

        """
        self.swagger_types = {
            'action_type': 'str',
            'action_details': 'ScheduleHttpActionDetails'
        }
        self.attribute_map = {
            'action_type': 'actionType',
            'action_details': 'actionDetails'
        }
        self._action_type = None
        self._action_details = None
        self._action_type = 'HTTP'

    @property
    def action_details(self):
        """
        **[Required]** Gets the action_details of this ScheduleHttpAction.

        :return: The action_details of this ScheduleHttpAction.
        :rtype: oci.data_science.models.ScheduleHttpActionDetails
        """
        return self._action_details

    @action_details.setter
    def action_details(self, action_details):
        """
        Sets the action_details of this ScheduleHttpAction.

        :param action_details: The action_details of this ScheduleHttpAction.
        :type: oci.data_science.models.ScheduleHttpActionDetails
        """
        self._action_details = action_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
