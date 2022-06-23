# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .forwarded_routing_configuration import ForwardedRoutingConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VcnRoutingConfiguration(ForwardedRoutingConfiguration):
    """
    Identifies the VCN route table and rule that allowed the traffic to be forwarded.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VcnRoutingConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.VcnRoutingConfiguration.type` attribute
        of this class is ``VCN`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VcnRoutingConfiguration.
            Allowed values for this property are: "VCN", "DRG"
        :type type: str

        :param vcn_route_table_id:
            The value to assign to the vcn_route_table_id property of this VcnRoutingConfiguration.
        :type vcn_route_table_id: str

        :param route_rule:
            The value to assign to the route_rule property of this VcnRoutingConfiguration.
        :type route_rule: oci.vn_monitoring.models.RouteRule

        """
        self.swagger_types = {
            'type': 'str',
            'vcn_route_table_id': 'str',
            'route_rule': 'RouteRule'
        }

        self.attribute_map = {
            'type': 'type',
            'vcn_route_table_id': 'vcnRouteTableId',
            'route_rule': 'routeRule'
        }

        self._type = None
        self._vcn_route_table_id = None
        self._route_rule = None
        self._type = 'VCN'

    @property
    def vcn_route_table_id(self):
        """
        **[Required]** Gets the vcn_route_table_id of this VcnRoutingConfiguration.
        The `OCID`__ of the VCN route
        table that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_route_table_id of this VcnRoutingConfiguration.
        :rtype: str
        """
        return self._vcn_route_table_id

    @vcn_route_table_id.setter
    def vcn_route_table_id(self, vcn_route_table_id):
        """
        Sets the vcn_route_table_id of this VcnRoutingConfiguration.
        The `OCID`__ of the VCN route
        table that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_route_table_id: The vcn_route_table_id of this VcnRoutingConfiguration.
        :type: str
        """
        self._vcn_route_table_id = vcn_route_table_id

    @property
    def route_rule(self):
        """
        **[Required]** Gets the route_rule of this VcnRoutingConfiguration.

        :return: The route_rule of this VcnRoutingConfiguration.
        :rtype: oci.vn_monitoring.models.RouteRule
        """
        return self._route_rule

    @route_rule.setter
    def route_rule(self, route_rule):
        """
        Sets the route_rule of this VcnRoutingConfiguration.

        :param route_rule: The route_rule of this VcnRoutingConfiguration.
        :type: oci.vn_monitoring.models.RouteRule
        """
        self._route_rule = route_rule

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
