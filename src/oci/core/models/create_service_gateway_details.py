# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateServiceGatewayDetails(object):
    """
    CreateServiceGatewayDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateServiceGatewayDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateServiceGatewayDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateServiceGatewayDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateServiceGatewayDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateServiceGatewayDetails.
        :type freeform_tags: dict(str, str)

        :param route_table_id:
            The value to assign to the route_table_id property of this CreateServiceGatewayDetails.
        :type route_table_id: str

        :param services:
            The value to assign to the services property of this CreateServiceGatewayDetails.
        :type services: list[oci.core.models.ServiceIdRequestDetails]

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateServiceGatewayDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'route_table_id': 'str',
            'services': 'list[ServiceIdRequestDetails]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'route_table_id': 'routeTableId',
            'services': 'services',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._route_table_id = None
        self._services = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateServiceGatewayDetails.
        The `OCID]`__ of the compartment to contain the service gateway.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateServiceGatewayDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateServiceGatewayDetails.
        The `OCID]`__ of the compartment to contain the service gateway.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateServiceGatewayDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateServiceGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateServiceGatewayDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateServiceGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateServiceGatewayDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateServiceGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateServiceGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateServiceGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateServiceGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateServiceGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateServiceGatewayDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateServiceGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateServiceGatewayDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this CreateServiceGatewayDetails.
        The `OCID`__ of the route table the service gateway will use.

        If you don't specify a route table here, the service gateway is created without an associated route
        table. The Networking service does NOT automatically associate the attached VCN's default route table
        with the service gateway.

        For information about why you would associate a route table with a service gateway, see
        `Transit Routing: Private Access to Oracle Services`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :return: The route_table_id of this CreateServiceGatewayDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this CreateServiceGatewayDetails.
        The `OCID`__ of the route table the service gateway will use.

        If you don't specify a route table here, the service gateway is created without an associated route
        table. The Networking service does NOT automatically associate the attached VCN's default route table
        with the service gateway.

        For information about why you would associate a route table with a service gateway, see
        `Transit Routing: Private Access to Oracle Services`__.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm
        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitroutingoracleservices.htm


        :param route_table_id: The route_table_id of this CreateServiceGatewayDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def services(self):
        """
        **[Required]** Gets the services of this CreateServiceGatewayDetails.
        List of the OCIDs of the :class:`Service` objects to
        enable for the service gateway. This list can be empty if you don't want to enable any
        `Service` objects when you create the gateway. You can enable a `Service`
        object later by using either :func:`attach_service_id`
        or :func:`update_service_gateway`.

        For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock`
        as the rule's destination and the service gateway as the rule's target. See
        :class:`RouteTable`.


        :return: The services of this CreateServiceGatewayDetails.
        :rtype: list[oci.core.models.ServiceIdRequestDetails]
        """
        return self._services

    @services.setter
    def services(self, services):
        """
        Sets the services of this CreateServiceGatewayDetails.
        List of the OCIDs of the :class:`Service` objects to
        enable for the service gateway. This list can be empty if you don't want to enable any
        `Service` objects when you create the gateway. You can enable a `Service`
        object later by using either :func:`attach_service_id`
        or :func:`update_service_gateway`.

        For each enabled `Service`, make sure there's a route rule with the `Service` object's `cidrBlock`
        as the rule's destination and the service gateway as the rule's target. See
        :class:`RouteTable`.


        :param services: The services of this CreateServiceGatewayDetails.
        :type: list[oci.core.models.ServiceIdRequestDetails]
        """
        self._services = services

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateServiceGatewayDetails.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this CreateServiceGatewayDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateServiceGatewayDetails.
        The `OCID`__ of the VCN.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this CreateServiceGatewayDetails.
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
