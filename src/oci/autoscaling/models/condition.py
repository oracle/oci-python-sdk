# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Condition(object):
    """
    A rule that defines a specific autoscaling action to take (scale in or scale out) and the metric that triggers that action.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Condition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this Condition.
        :type action: Action

        :param display_name:
            The value to assign to the display_name property of this Condition.
        :type display_name: str

        :param id:
            The value to assign to the id property of this Condition.
        :type id: str

        :param metric:
            The value to assign to the metric property of this Condition.
        :type metric: Metric

        """
        self.swagger_types = {
            'action': 'Action',
            'display_name': 'str',
            'id': 'str',
            'metric': 'Metric'
        }

        self.attribute_map = {
            'action': 'action',
            'display_name': 'displayName',
            'id': 'id',
            'metric': 'metric'
        }

        self._action = None
        self._display_name = None
        self._id = None
        self._metric = None

    @property
    def action(self):
        """
        **[Required]** Gets the action of this Condition.

        :return: The action of this Condition.
        :rtype: Action
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this Condition.

        :param action: The action of this Condition.
        :type: Action
        """
        self._action = action

    @property
    def display_name(self):
        """
        Gets the display_name of this Condition.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this Condition.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Condition.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this Condition.
        :type: str
        """
        self._display_name = display_name

    @property
    def id(self):
        """
        Gets the id of this Condition.
        ID of the condition that is assigned after creation.


        :return: The id of this Condition.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Condition.
        ID of the condition that is assigned after creation.


        :param id: The id of this Condition.
        :type: str
        """
        self._id = id

    @property
    def metric(self):
        """
        **[Required]** Gets the metric of this Condition.

        :return: The metric of this Condition.
        :rtype: Metric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """
        Sets the metric of this Condition.

        :param metric: The metric of this Condition.
        :type: Metric
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
