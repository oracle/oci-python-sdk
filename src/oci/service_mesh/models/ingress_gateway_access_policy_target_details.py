# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .access_policy_target_details import AccessPolicyTargetDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressGatewayAccessPolicyTargetDetails(AccessPolicyTargetDetails):
    """
    Ingress gateway target that virtual services in mesh receive traffic from.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IngressGatewayAccessPolicyTargetDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.service_mesh.models.IngressGatewayAccessPolicyTargetDetails.type` attribute
        of this class is ``INGRESS_GATEWAY`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this IngressGatewayAccessPolicyTargetDetails.
            Allowed values for this property are: "ALL_VIRTUAL_SERVICES", "VIRTUAL_SERVICE", "EXTERNAL_SERVICE", "INGRESS_GATEWAY"
        :type type: str

        :param ingress_gateway_id:
            The value to assign to the ingress_gateway_id property of this IngressGatewayAccessPolicyTargetDetails.
        :type ingress_gateway_id: str

        """
        self.swagger_types = {
            'type': 'str',
            'ingress_gateway_id': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'ingress_gateway_id': 'ingressGatewayId'
        }

        self._type = None
        self._ingress_gateway_id = None
        self._type = 'INGRESS_GATEWAY'

    @property
    def ingress_gateway_id(self):
        """
        **[Required]** Gets the ingress_gateway_id of this IngressGatewayAccessPolicyTargetDetails.
        The OCID of the ingress gateway resource.


        :return: The ingress_gateway_id of this IngressGatewayAccessPolicyTargetDetails.
        :rtype: str
        """
        return self._ingress_gateway_id

    @ingress_gateway_id.setter
    def ingress_gateway_id(self, ingress_gateway_id):
        """
        Sets the ingress_gateway_id of this IngressGatewayAccessPolicyTargetDetails.
        The OCID of the ingress gateway resource.


        :param ingress_gateway_id: The ingress_gateway_id of this IngressGatewayAccessPolicyTargetDetails.
        :type: str
        """
        self._ingress_gateway_id = ingress_gateway_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
