# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgRouteDistributionStatement(object):
    """
    A single statement within a route distribution. All match criteria in a statement must be met
    for the action to take place.
    """

    #: A constant which can be used with the action property of a DrgRouteDistributionStatement.
    #: This constant has a value of "ACCEPT"
    ACTION_ACCEPT = "ACCEPT"

    def __init__(self, **kwargs):
        """
        Initializes a new DrgRouteDistributionStatement object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param match_criteria:
            The value to assign to the match_criteria property of this DrgRouteDistributionStatement.
        :type match_criteria: list[oci.vn_monitoring.models.DrgRouteDistributionMatchCriteria]

        :param action:
            The value to assign to the action property of this DrgRouteDistributionStatement.
            Allowed values for this property are: "ACCEPT"
        :type action: str

        :param priority:
            The value to assign to the priority property of this DrgRouteDistributionStatement.
        :type priority: int

        :param id:
            The value to assign to the id property of this DrgRouteDistributionStatement.
        :type id: str

        """
        self.swagger_types = {
            'match_criteria': 'list[DrgRouteDistributionMatchCriteria]',
            'action': 'str',
            'priority': 'int',
            'id': 'str'
        }

        self.attribute_map = {
            'match_criteria': 'matchCriteria',
            'action': 'action',
            'priority': 'priority',
            'id': 'id'
        }

        self._match_criteria = None
        self._action = None
        self._priority = None
        self._id = None

    @property
    def match_criteria(self):
        """
        **[Required]** Gets the match_criteria of this DrgRouteDistributionStatement.
        The action is applied only if all of the match criteria is met.
        If there are no match criteria in a statement, any input is considered a match and the action is applied.


        :return: The match_criteria of this DrgRouteDistributionStatement.
        :rtype: list[oci.vn_monitoring.models.DrgRouteDistributionMatchCriteria]
        """
        return self._match_criteria

    @match_criteria.setter
    def match_criteria(self, match_criteria):
        """
        Sets the match_criteria of this DrgRouteDistributionStatement.
        The action is applied only if all of the match criteria is met.
        If there are no match criteria in a statement, any input is considered a match and the action is applied.


        :param match_criteria: The match_criteria of this DrgRouteDistributionStatement.
        :type: list[oci.vn_monitoring.models.DrgRouteDistributionMatchCriteria]
        """
        self._match_criteria = match_criteria

    @property
    def action(self):
        """
        **[Required]** Gets the action of this DrgRouteDistributionStatement.
        `ACCEPT` indicates the route should be imported or exported as-is.

        Allowed values for this property are: "ACCEPT"


        :return: The action of this DrgRouteDistributionStatement.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this DrgRouteDistributionStatement.
        `ACCEPT` indicates the route should be imported or exported as-is.


        :param action: The action of this DrgRouteDistributionStatement.
        :type: str
        """
        allowed_values = ["ACCEPT"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            raise ValueError(
                "Invalid value for `action`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._action = action

    @property
    def priority(self):
        """
        **[Required]** Gets the priority of this DrgRouteDistributionStatement.
        This field specifies the priority of each statement in a route distribution.
        Priorities must be unique within a particular route distribution.
        The priority will be represented as a number between 0 and 65535 where a lower number
        indicates a higher priority. When a route is processed, statements are applied in the order
        defined by their priority. The first matching rule dictates the action that will be taken
        on the route.


        :return: The priority of this DrgRouteDistributionStatement.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this DrgRouteDistributionStatement.
        This field specifies the priority of each statement in a route distribution.
        Priorities must be unique within a particular route distribution.
        The priority will be represented as a number between 0 and 65535 where a lower number
        indicates a higher priority. When a route is processed, statements are applied in the order
        defined by their priority. The first matching rule dictates the action that will be taken
        on the route.


        :param priority: The priority of this DrgRouteDistributionStatement.
        :type: int
        """
        self._priority = priority

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DrgRouteDistributionStatement.
        The Oracle-assigned ID of the route distribution statement.


        :return: The id of this DrgRouteDistributionStatement.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DrgRouteDistributionStatement.
        The Oracle-assigned ID of the route distribution statement.


        :param id: The id of this DrgRouteDistributionStatement.
        :type: str
        """
        self._id = id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
