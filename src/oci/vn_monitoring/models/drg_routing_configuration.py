# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .forwarded_routing_configuration import ForwardedRoutingConfiguration
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DrgRoutingConfiguration(ForwardedRoutingConfiguration):
    """
    Identifies the DRG route table and rule that allowed the traffic to be forwarded.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DrgRoutingConfiguration object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.DrgRoutingConfiguration.type` attribute
        of this class is ``DRG`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this DrgRoutingConfiguration.
            Allowed values for this property are: "VCN", "DRG"
        :type type: str

        :param drg_route_table_id:
            The value to assign to the drg_route_table_id property of this DrgRoutingConfiguration.
        :type drg_route_table_id: str

        :param route_rule:
            The value to assign to the route_rule property of this DrgRoutingConfiguration.
        :type route_rule: oci.vn_monitoring.models.DrgRouteRule

        """
        self.swagger_types = {
            'type': 'str',
            'drg_route_table_id': 'str',
            'route_rule': 'DrgRouteRule'
        }
        self.attribute_map = {
            'type': 'type',
            'drg_route_table_id': 'drgRouteTableId',
            'route_rule': 'routeRule'
        }
        self._type = None
        self._drg_route_table_id = None
        self._route_rule = None
        self._type = 'DRG'

    @property
    def drg_route_table_id(self):
        """
        **[Required]** Gets the drg_route_table_id of this DrgRoutingConfiguration.
        The `OCID`__ of the DRG route
        table that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The drg_route_table_id of this DrgRoutingConfiguration.
        :rtype: str
        """
        return self._drg_route_table_id

    @drg_route_table_id.setter
    def drg_route_table_id(self, drg_route_table_id):
        """
        Sets the drg_route_table_id of this DrgRoutingConfiguration.
        The `OCID`__ of the DRG route
        table that allowed the traffic.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param drg_route_table_id: The drg_route_table_id of this DrgRoutingConfiguration.
        :type: str
        """
        self._drg_route_table_id = drg_route_table_id

    @property
    def route_rule(self):
        """
        **[Required]** Gets the route_rule of this DrgRoutingConfiguration.

        :return: The route_rule of this DrgRoutingConfiguration.
        :rtype: oci.vn_monitoring.models.DrgRouteRule
        """
        return self._route_rule

    @route_rule.setter
    def route_rule(self, route_rule):
        """
        Sets the route_rule of this DrgRoutingConfiguration.

        :param route_rule: The route_rule of this DrgRoutingConfiguration.
        :type: oci.vn_monitoring.models.DrgRouteRule
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
