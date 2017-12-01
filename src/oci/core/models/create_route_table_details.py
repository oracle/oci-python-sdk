# coding: utf-8
# Copyright (c) 2016, 2017, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateRouteTableDetails(object):

    def __init__(self, **kwargs):
        """
        Initializes a new CreateRouteTableDetails object with values from values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateRouteTableDetails.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this CreateRouteTableDetails.
        :type display_name: str

        :param route_rules:
            The value to assign to the route_rules property of this CreateRouteTableDetails.
        :type route_rules: list[RouteRule]

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateRouteTableDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'route_rules': 'list[RouteRule]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'route_rules': 'routeRules',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
        self._route_rules = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateRouteTableDetails.
        The OCID of the compartment to contain the route table.


        :return: The compartment_id of this CreateRouteTableDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateRouteTableDetails.
        The OCID of the compartment to contain the route table.


        :param compartment_id: The compartment_id of this CreateRouteTableDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateRouteTableDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateRouteTableDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateRouteTableDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def route_rules(self):
        """
        Gets the route_rules of this CreateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.


        :return: The route_rules of this CreateRouteTableDetails.
        :rtype: list[RouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this CreateRouteTableDetails.
        The collection of rules used for routing destination IPs to network devices.


        :param route_rules: The route_rules of this CreateRouteTableDetails.
        :type: list[RouteRule]
        """
        self._route_rules = route_rules

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateRouteTableDetails.
        The OCID of the VCN the route table belongs to.


        :return: The vcn_id of this CreateRouteTableDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateRouteTableDetails.
        The OCID of the VCN the route table belongs to.


        :param vcn_id: The vcn_id of this CreateRouteTableDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
