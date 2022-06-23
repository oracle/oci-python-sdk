# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .routing_action import RoutingAction
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ForwardedRoutingAction(RoutingAction):
    """
    Defines the routing actions taken for traffic that is forwarded.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ForwardedRoutingAction object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.ForwardedRoutingAction.action` attribute
        of this class is ``FORWARDED`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param action:
            The value to assign to the action property of this ForwardedRoutingAction.
            Allowed values for this property are: "FORWARDED", "NO_ROUTE", "INDETERMINATE"
        :type action: str

        :param action_type:
            The value to assign to the action_type property of this ForwardedRoutingAction.
            Allowed values for this property are: "EXPLICIT", "IMPLICIT", "NOT_SUPPORTED"
        :type action_type: str

        :param forwarded_routing_action_details:
            The value to assign to the forwarded_routing_action_details property of this ForwardedRoutingAction.
        :type forwarded_routing_action_details: oci.vn_monitoring.models.ForwardedRoutingActionDetails

        """
        self.swagger_types = {
            'action': 'str',
            'action_type': 'str',
            'forwarded_routing_action_details': 'ForwardedRoutingActionDetails'
        }

        self.attribute_map = {
            'action': 'action',
            'action_type': 'actionType',
            'forwarded_routing_action_details': 'forwardedRoutingActionDetails'
        }

        self._action = None
        self._action_type = None
        self._forwarded_routing_action_details = None
        self._action = 'FORWARDED'

    @property
    def forwarded_routing_action_details(self):
        """
        Gets the forwarded_routing_action_details of this ForwardedRoutingAction.

        :return: The forwarded_routing_action_details of this ForwardedRoutingAction.
        :rtype: oci.vn_monitoring.models.ForwardedRoutingActionDetails
        """
        return self._forwarded_routing_action_details

    @forwarded_routing_action_details.setter
    def forwarded_routing_action_details(self, forwarded_routing_action_details):
        """
        Sets the forwarded_routing_action_details of this ForwardedRoutingAction.

        :param forwarded_routing_action_details: The forwarded_routing_action_details of this ForwardedRoutingAction.
        :type: oci.vn_monitoring.models.ForwardedRoutingActionDetails
        """
        self._forwarded_routing_action_details = forwarded_routing_action_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
