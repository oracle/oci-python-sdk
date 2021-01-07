# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateConditionDetails(object):
    """
    Update details for a condition in a threshold-based autoscaling policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateConditionDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this UpdateConditionDetails.
        :type action: oci.autoscaling.models.Action

        :param display_name:
            The value to assign to the display_name property of this UpdateConditionDetails.
        :type display_name: str

        :param metric:
            The value to assign to the metric property of this UpdateConditionDetails.
        :type metric: oci.autoscaling.models.Metric

        """
        self.swagger_types = {
            'action': 'Action',
            'display_name': 'str',
            'metric': 'Metric'
        }

        self.attribute_map = {
            'action': 'action',
            'display_name': 'displayName',
            'metric': 'metric'
        }

        self._action = None
        self._display_name = None
        self._metric = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this UpdateConditionDetails.

        :return: The action of this UpdateConditionDetails.
        :rtype: oci.autoscaling.models.Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this UpdateConditionDetails.

        :param action: The action of this UpdateConditionDetails.
        :type: oci.autoscaling.models.Action
        """
        self._action = action

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateConditionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this UpdateConditionDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateConditionDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this UpdateConditionDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def metric(self):
        """
        **[Required]** Gets the metric of this UpdateConditionDetails.

        :return: The metric of this UpdateConditionDetails.
        :rtype: oci.autoscaling.models.Metric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this UpdateConditionDetails.

        :param metric: The metric of this UpdateConditionDetails.
        :type: oci.autoscaling.models.Metric
        """
        self._metric = metric

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
