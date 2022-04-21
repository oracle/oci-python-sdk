# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateIngressGatewayRouteTableDetails(object):
    """
    The information about a new IngressGatewayRouteTable.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateIngressGatewayRouteTableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ingress_gateway_id:
            The value to assign to the ingress_gateway_id property of this CreateIngressGatewayRouteTableDetails.
        :type ingress_gateway_id: str

        :param name:
            The value to assign to the name property of this CreateIngressGatewayRouteTableDetails.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateIngressGatewayRouteTableDetails.
        :type description: str

        :param priority:
            The value to assign to the priority property of this CreateIngressGatewayRouteTableDetails.
        :type priority: int

        :param route_rules:
            The value to assign to the route_rules property of this CreateIngressGatewayRouteTableDetails.
        :type route_rules: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateIngressGatewayRouteTableDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateIngressGatewayRouteTableDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateIngressGatewayRouteTableDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'ingress_gateway_id': 'str',
            'name': 'str',
            'description': 'str',
            'priority': 'int',
            'route_rules': 'list[IngressGatewayTrafficRouteRule]',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'ingress_gateway_id': 'ingressGatewayId',
            'name': 'name',
            'description': 'description',
            'priority': 'priority',
            'route_rules': 'routeRules',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._ingress_gateway_id = None
        self._name = None
        self._description = None
        self._priority = None
        self._route_rules = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def ingress_gateway_id(self):
        """
        **[Required]** Gets the ingress_gateway_id of this CreateIngressGatewayRouteTableDetails.
        The OCID of the service mesh in which this access policy is created.


        :return: The ingress_gateway_id of this CreateIngressGatewayRouteTableDetails.
        :rtype: str
        """
        return self._ingress_gateway_id

    @ingress_gateway_id.setter
    def ingress_gateway_id(self, ingress_gateway_id):
        """
        Sets the ingress_gateway_id of this CreateIngressGatewayRouteTableDetails.
        The OCID of the service mesh in which this access policy is created.


        :param ingress_gateway_id: The ingress_gateway_id of this CreateIngressGatewayRouteTableDetails.
        :type: str
        """
        self._ingress_gateway_id = ingress_gateway_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateIngressGatewayRouteTableDetails.
        A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :return: The name of this CreateIngressGatewayRouteTableDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateIngressGatewayRouteTableDetails.
        A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :param name: The name of this CreateIngressGatewayRouteTableDetails.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this CreateIngressGatewayRouteTableDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this CreateIngressGatewayRouteTableDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateIngressGatewayRouteTableDetails.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this CreateIngressGatewayRouteTableDetails.
        :type: str
        """
        self._description = description

    @property
    def priority(self):
        """
        Gets the priority of this CreateIngressGatewayRouteTableDetails.
        The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.


        :return: The priority of this CreateIngressGatewayRouteTableDetails.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this CreateIngressGatewayRouteTableDetails.
        The priority of the route table. Lower value means higher priority. The routes are declared based on the priority.


        :param priority: The priority of this CreateIngressGatewayRouteTableDetails.
        :type: int
        """
        self._priority = priority

    @property
    def route_rules(self):
        """
        **[Required]** Gets the route_rules of this CreateIngressGatewayRouteTableDetails.
        The route rules for the ingress gateway.


        :return: The route_rules of this CreateIngressGatewayRouteTableDetails.
        :rtype: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this CreateIngressGatewayRouteTableDetails.
        The route rules for the ingress gateway.


        :param route_rules: The route_rules of this CreateIngressGatewayRouteTableDetails.
        :type: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]
        """
        self._route_rules = route_rules

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateIngressGatewayRouteTableDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateIngressGatewayRouteTableDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateIngressGatewayRouteTableDetails.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateIngressGatewayRouteTableDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateIngressGatewayRouteTableDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateIngressGatewayRouteTableDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateIngressGatewayRouteTableDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateIngressGatewayRouteTableDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateIngressGatewayRouteTableDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateIngressGatewayRouteTableDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateIngressGatewayRouteTableDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateIngressGatewayRouteTableDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
