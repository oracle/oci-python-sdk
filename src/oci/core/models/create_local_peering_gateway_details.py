# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from ...util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from ...decorators import init_model_state_from_kwargs


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

        :param display_name:
            The value to assign to the display_name property of this CreateLocalPeeringGatewayDetails.
        :type display_name: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateLocalPeeringGatewayDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._display_name = None
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
