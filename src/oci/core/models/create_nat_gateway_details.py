# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateNatGatewayDetails(object):
    """
    CreateNatGatewayDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateNatGatewayDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateNatGatewayDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateNatGatewayDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateNatGatewayDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateNatGatewayDetails.
        :type freeform_tags: dict(str, str)

        :param block_traffic:
            The value to assign to the block_traffic property of this CreateNatGatewayDetails.
        :type block_traffic: bool

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateNatGatewayDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'block_traffic': 'bool',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'block_traffic': 'blockTraffic',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._block_traffic = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateNatGatewayDetails.
        The `OCID`__ of the compartment to contain the
        NAT gateway.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this CreateNatGatewayDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateNatGatewayDetails.
        The `OCID`__ of the compartment to contain the
        NAT gateway.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this CreateNatGatewayDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateNatGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateNatGatewayDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateNatGatewayDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateNatGatewayDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateNatGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this CreateNatGatewayDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateNatGatewayDetails.
        A user-friendly name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this CreateNatGatewayDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateNatGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateNatGatewayDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateNatGatewayDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateNatGatewayDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def block_traffic(self):
        """
        Gets the block_traffic of this CreateNatGatewayDetails.
        Whether the NAT gateway blocks traffic through it. The default is `false`.

        Example: `true`


        :return: The block_traffic of this CreateNatGatewayDetails.
        :rtype: bool
        """
        return self._block_traffic

    @block_traffic.setter
    def block_traffic(self, block_traffic):
        """
        Sets the block_traffic of this CreateNatGatewayDetails.
        Whether the NAT gateway blocks traffic through it. The default is `false`.

        Example: `true`


        :param block_traffic: The block_traffic of this CreateNatGatewayDetails.
        :type: bool
        """
        self._block_traffic = block_traffic

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateNatGatewayDetails.
        The `OCID`__ of the VCN the gateway belongs to.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this CreateNatGatewayDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateNatGatewayDetails.
        The `OCID`__ of the VCN the gateway belongs to.

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this CreateNatGatewayDetails.
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
