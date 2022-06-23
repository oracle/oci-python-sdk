# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateDrgRouteRulesDetails(object):
    """
    Details used to update route rules in a DRG route table.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateDrgRouteRulesDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param route_rules:
            The value to assign to the route_rules property of this UpdateDrgRouteRulesDetails.
        :type route_rules: list[oci.vn_monitoring.models.UpdateDrgRouteRuleDetails]

        """
        self.swagger_types = {
            'route_rules': 'list[UpdateDrgRouteRuleDetails]'
        }

        self.attribute_map = {
            'route_rules': 'routeRules'
        }

        self._route_rules = None

    @property
    def route_rules(self):
        """
        Gets the route_rules of this UpdateDrgRouteRulesDetails.
        The DRG rute rules to update.


        :return: The route_rules of this UpdateDrgRouteRulesDetails.
        :rtype: list[oci.vn_monitoring.models.UpdateDrgRouteRuleDetails]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this UpdateDrgRouteRulesDetails.
        The DRG rute rules to update.


        :param route_rules: The route_rules of this UpdateDrgRouteRulesDetails.
        :type: list[oci.vn_monitoring.models.UpdateDrgRouteRuleDetails]
        """
        self._route_rules = route_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
