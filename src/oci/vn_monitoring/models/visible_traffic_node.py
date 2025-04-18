# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20160918

from .traffic_node import TrafficNode
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VisibleTrafficNode(TrafficNode):
    """
    Defines the configuration of a traffic node that is visible to the user.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VisibleTrafficNode object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.VisibleTrafficNode.type` attribute
        of this class is ``VISIBLE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this VisibleTrafficNode.
            Allowed values for this property are: "VISIBLE", "ACCESS_DENIED"
        :type type: str

        :param egress_traffic:
            The value to assign to the egress_traffic property of this VisibleTrafficNode.
        :type egress_traffic: oci.vn_monitoring.models.EgressTrafficSpec

        :param next_hop_routing_action:
            The value to assign to the next_hop_routing_action property of this VisibleTrafficNode.
        :type next_hop_routing_action: oci.vn_monitoring.models.RoutingAction

        :param egress_security_action:
            The value to assign to the egress_security_action property of this VisibleTrafficNode.
        :type egress_security_action: oci.vn_monitoring.models.SecurityAction

        :param ingress_security_action:
            The value to assign to the ingress_security_action property of this VisibleTrafficNode.
        :type ingress_security_action: oci.vn_monitoring.models.SecurityAction

        :param entity_id:
            The value to assign to the entity_id property of this VisibleTrafficNode.
        :type entity_id: str

        :param transformation_description:
            The value to assign to the transformation_description property of this VisibleTrafficNode.
        :type transformation_description: str

        """
        self.swagger_types = {
            'type': 'str',
            'egress_traffic': 'EgressTrafficSpec',
            'next_hop_routing_action': 'RoutingAction',
            'egress_security_action': 'SecurityAction',
            'ingress_security_action': 'SecurityAction',
            'entity_id': 'str',
            'transformation_description': 'str'
        }
        self.attribute_map = {
            'type': 'type',
            'egress_traffic': 'egressTraffic',
            'next_hop_routing_action': 'nextHopRoutingAction',
            'egress_security_action': 'egressSecurityAction',
            'ingress_security_action': 'ingressSecurityAction',
            'entity_id': 'entityId',
            'transformation_description': 'transformationDescription'
        }
        self._type = None
        self._egress_traffic = None
        self._next_hop_routing_action = None
        self._egress_security_action = None
        self._ingress_security_action = None
        self._entity_id = None
        self._transformation_description = None
        self._type = 'VISIBLE'

    @property
    def entity_id(self):
        """
        Gets the entity_id of this VisibleTrafficNode.
        The `OCID`__ of the OCI entity that
        represents the traffic node (Instance, GW, LB, etc.).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The entity_id of this VisibleTrafficNode.
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """
        Sets the entity_id of this VisibleTrafficNode.
        The `OCID`__ of the OCI entity that
        represents the traffic node (Instance, GW, LB, etc.).

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param entity_id: The entity_id of this VisibleTrafficNode.
        :type: str
        """
        self._entity_id = entity_id

    @property
    def transformation_description(self):
        """
        Gets the transformation_description of this VisibleTrafficNode.
        Describes how the traffic was transformed. For example, if an address is translated by a NAT GW,
        the string will describe the translation: 'SNAT: 10.0.0.1->204.0.0.1'


        :return: The transformation_description of this VisibleTrafficNode.
        :rtype: str
        """
        return self._transformation_description

    @transformation_description.setter
    def transformation_description(self, transformation_description):
        """
        Sets the transformation_description of this VisibleTrafficNode.
        Describes how the traffic was transformed. For example, if an address is translated by a NAT GW,
        the string will describe the translation: 'SNAT: 10.0.0.1->204.0.0.1'


        :param transformation_description: The transformation_description of this VisibleTrafficNode.
        :type: str
        """
        self._transformation_description = transformation_description

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
