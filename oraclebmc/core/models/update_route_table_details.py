# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict


class UpdateRouteTableDetails(object):

    def __init__(self):

        self.swagger_types = {
            'display_name': 'str',
            'route_rules': 'list[RouteRule]'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'route_rules': 'routeRules'
        }

        self._display_name = None
        self._route_rules = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :return: The display_name of this UpdateRouteTableDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.


        :param display_name: The display_name of this UpdateRouteTableDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def route_rules(self):
        """
        Gets the route_rules of this UpdateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.


        :return: The route_rules of this UpdateRouteTableDetails.
        :rtype: list[RouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this UpdateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.


        :param route_rules: The route_rules of this UpdateRouteTableDetails.
        :type: list[RouteRule]
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
