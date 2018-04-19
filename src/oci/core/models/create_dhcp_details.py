# coding: utf-8
# Copyright (c) 2016, 2018, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDhcpDetails(object):
    """
    CreateDhcpDetails model.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDhcpDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDhcpDetails.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDhcpDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateDhcpDetails.
        :type display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDhcpDetails.
        :type freeform_tags: dict(str, str)

        :param options:
            The value to assign to the options property of this CreateDhcpDetails.
        :type options: list[DhcpOption]

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateDhcpDetails.
        :type vcn_id: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'options': 'list[DhcpOption]',
            'vcn_id': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'display_name': 'displayName',
            'freeform_tags': 'freeformTags',
            'options': 'options',
            'vcn_id': 'vcnId'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._display_name = None
        self._freeform_tags = None
        self._options = None
        self._vcn_id = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDhcpDetails.
        The OCID of the compartment to contain the set of DHCP options.


        :return: The compartment_id of this CreateDhcpDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDhcpDetails.
        The OCID of the compartment to contain the set of DHCP options.


        :param compartment_id: The compartment_id of this CreateDhcpDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDhcpDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDhcpDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDhcpDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDhcpDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateDhcpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this CreateDhcpDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDhcpDetails.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this CreateDhcpDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDhcpDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDhcpDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDhcpDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no
        predefined name, type, or namespace. For more information, see
        `Resource Tags`__.

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDhcpDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def options(self):
        """
        **[Required]** Gets the options of this CreateDhcpDetails.
        A set of DHCP options.


        :return: The options of this CreateDhcpDetails.
        :rtype: list[DhcpOption]
        """
        return self._options

    @options.setter
    def options(self, options):
        """
        Sets the options of this CreateDhcpDetails.
        A set of DHCP options.


        :param options: The options of this CreateDhcpDetails.
        :type: list[DhcpOption]
        """
        self._options = options

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateDhcpDetails.
        The OCID of the VCN the set of DHCP options belongs to.


        :return: The vcn_id of this CreateDhcpDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateDhcpDetails.
        The OCID of the VCN the set of DHCP options belongs to.


        :param vcn_id: The vcn_id of this CreateDhcpDetails.
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
