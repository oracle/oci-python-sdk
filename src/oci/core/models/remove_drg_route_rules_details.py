# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RemoveDrgRouteRulesDetails(object):
    """
    Details used in a request to remove static routes from a DRG route table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RemoveDrgRouteRulesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param route_rule_ids:
            The value to assign to the route_rule_ids property of this RemoveDrgRouteRulesDetails.
        :type route_rule_ids: list[str]

        """
        self.swagger_types = {
            'route_rule_ids': 'list[str]'
        }

        self.attribute_map = {
            'route_rule_ids': 'routeRuleIds'
        }

        self._route_rule_ids = None

    @property
    def route_rule_ids(self):
        """
        Gets the route_rule_ids of this RemoveDrgRouteRulesDetails.
        The Oracle-assigned ID of each DRG route rule to be deleted.


        :return: The route_rule_ids of this RemoveDrgRouteRulesDetails.
        :rtype: list[str]
        """
        return self._route_rule_ids

    @route_rule_ids.setter
    def route_rule_ids(self, route_rule_ids):
        """
        Sets the route_rule_ids of this RemoveDrgRouteRulesDetails.
        The Oracle-assigned ID of each DRG route rule to be deleted.


        :param route_rule_ids: The route_rule_ids of this RemoveDrgRouteRulesDetails.
        :type: list[str]
        """
        self._route_rule_ids = route_rule_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
