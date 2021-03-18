# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateLocalPeeringGatewayDetails(object):
    """
    CreateLocalPeeringGatewayDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateLocalPeeringGatewayDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateLocalPeeringGatewayDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateLocalPeeringGatewayDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateLocalPeeringGatewayDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateLocalPeeringGatewayDetails.
        :type freeform_tags: dict(str, str)

        :param route_table_id:
            The value to assign to the route_table_id property of this CreateLocalPeeringGatewayDetails.
        :type route_table_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateLocalPeeringGatewayDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'route_table_id': 'str',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'route_table_id': 'routeTableId',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._route_table_id = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateLocalPeeringGatewayDetails.
        The OCID of the compartment containing the local peering gateway (LPG).


        :return: The compartment_id of this CreateLocalPeeringGatewayDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateLocalPeeringGatewayDetails.
        The OCID of the compartment containing the local peering gateway (LPG).


        :param compartment_id: The compartment_id of this CreateLocalPeeringGatewayDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateLocalPeeringGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateLocalPeeringGatewayDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateLocalPeeringGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a
        namespace. For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateLocalPeeringGatewayDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateLocalPeeringGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :return: The display_name of this CreateLocalPeeringGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateLocalPeeringGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid
        entering confidential information.


        :param display_name: The display_name of this CreateLocalPeeringGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateLocalPeeringGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateLocalPeeringGatewayDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateLocalPeeringGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateLocalPeeringGatewayDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def route_table_id(self):
        """
        Gets the route_table_id of this CreateLocalPeeringGatewayDetails.
        The OCID of the route table the LPG will use.

        If you don't specify a route table here, the LPG is created without an associated route
        table. The Networking service does NOT automatically associate the attached VCN's default route table
        with the LPG.

        For information about why you would associate a route table with an LPG, see
        `Transit Routing: Access to Multiple VCNs in Same Region`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm


        :return: The route_table_id of this CreateLocalPeeringGatewayDetails.
        :rtype: str
        """
        return self._route_table_id

    @route_table_id.setter
    def route_table_id(self, route_table_id):
        """
        Sets the route_table_id of this CreateLocalPeeringGatewayDetails.
        The OCID of the route table the LPG will use.

        If you don't specify a route table here, the LPG is created without an associated route
        table. The Networking service does NOT automatically associate the attached VCN's default route table
        with the LPG.

        For information about why you would associate a route table with an LPG, see
        `Transit Routing: Access to Multiple VCNs in Same Region`__.

        __ https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm


        :param route_table_id: The route_table_id of this CreateLocalPeeringGatewayDetails.
        :type: str
        """
        self._route_table_id = route_table_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateLocalPeeringGatewayDetails.
        The OCID of the VCN the LPG belongs to.


        :return: The vcn_id of this CreateLocalPeeringGatewayDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateLocalPeeringGatewayDetails.
        The OCID of the VCN the LPG belongs to.


        :param vcn_id: The vcn_id of this CreateLocalPeeringGatewayDetails.
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
