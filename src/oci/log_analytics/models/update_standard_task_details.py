# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .update_scheduled_task_details import UpdateScheduledTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateStandardTaskDetails(UpdateScheduledTaskDetails):
    """
    The details for updating a schedule task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateStandardTaskDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.log_analytics.models.UpdateStandardTaskDetails.kind` attribute
        of this class is ``STANDARD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this UpdateStandardTaskDetails.
            Allowed values for this property are: "ACCELERATION", "STANDARD"
        :type kind: str

        :param display_name:
            The value to assign to the display_name property of this UpdateStandardTaskDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateStandardTaskDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateStandardTaskDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param schedules:
            The value to assign to the schedules property of this UpdateStandardTaskDetails.
        :type schedules: list[oci.log_analytics.models.Schedule]

        :param action:
            The value to assign to the action property of this UpdateStandardTaskDetails.
        :type action: oci.log_analytics.models.Action

        """
        self.swagger_types = {
            'kind': 'str',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'schedules': 'list[Schedule]',
            'action': 'Action'
        }

        self.attribute_map = {
            'kind': 'kind',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'schedules': 'schedules',
            'action': 'action'
        }

        self._kind = None
        self._display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._schedules = None
        self._action = None
        self._kind = 'STANDARD'

    @property
    def action(self):
        """
        Gets the action of this UpdateStandardTaskDetails.

        :return: The action of this UpdateStandardTaskDetails.
        :rtype: oci.log_analytics.models.Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this UpdateStandardTaskDetails.

        :param action: The action of this UpdateStandardTaskDetails.
        :type: oci.log_analytics.models.Action
        """
        self._action = action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
