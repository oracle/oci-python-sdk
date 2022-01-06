# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateDataSafePrivateEndpointDetails(object):
    """
    The details used to create a new Data Safe private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateDataSafePrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this CreateDataSafePrivateEndpointDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateDataSafePrivateEndpointDetails.
        :type compartment_id: str

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateDataSafePrivateEndpointDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateDataSafePrivateEndpointDetails.
        :type subnet_id: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this CreateDataSafePrivateEndpointDetails.
        :type private_endpoint_ip: str

        :param description:
            The value to assign to the description property of this CreateDataSafePrivateEndpointDetails.
        :type description: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateDataSafePrivateEndpointDetails.
        :type nsg_ids: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateDataSafePrivateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateDataSafePrivateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'compartment_id': 'str',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'private_endpoint_ip': 'str',
            'description': 'str',
            'nsg_ids': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'private_endpoint_ip': 'privateEndpointIp',
            'description': 'description',
            'nsg_ids': 'nsgIds',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._compartment_id = None
        self._vcn_id = None
        self._subnet_id = None
        self._private_endpoint_ip = None
        self._description = None
        self._nsg_ids = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateDataSafePrivateEndpointDetails.
        The display name for the private endpoint. The name does not have to be unique, and it's changeable.


        :return: The display_name of this CreateDataSafePrivateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateDataSafePrivateEndpointDetails.
        The display name for the private endpoint. The name does not have to be unique, and it's changeable.


        :param display_name: The display_name of this CreateDataSafePrivateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateDataSafePrivateEndpointDetails.
        The OCID of the compartment.


        :return: The compartment_id of this CreateDataSafePrivateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateDataSafePrivateEndpointDetails.
        The OCID of the compartment.


        :param compartment_id: The compartment_id of this CreateDataSafePrivateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this CreateDataSafePrivateEndpointDetails.
        The OCID of the VCN.


        :return: The vcn_id of this CreateDataSafePrivateEndpointDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateDataSafePrivateEndpointDetails.
        The OCID of the VCN.


        :param vcn_id: The vcn_id of this CreateDataSafePrivateEndpointDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateDataSafePrivateEndpointDetails.
        The OCID of the subnet.


        :return: The subnet_id of this CreateDataSafePrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateDataSafePrivateEndpointDetails.
        The OCID of the subnet.


        :param subnet_id: The subnet_id of this CreateDataSafePrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this CreateDataSafePrivateEndpointDetails.
        The private IP address of the private endpoint.


        :return: The private_endpoint_ip of this CreateDataSafePrivateEndpointDetails.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this CreateDataSafePrivateEndpointDetails.
        The private IP address of the private endpoint.


        :param private_endpoint_ip: The private_endpoint_ip of this CreateDataSafePrivateEndpointDetails.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def description(self):
        """
        Gets the description of this CreateDataSafePrivateEndpointDetails.
        The description of the private endpoint.


        :return: The description of this CreateDataSafePrivateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateDataSafePrivateEndpointDetails.
        The description of the private endpoint.


        :param description: The description of this CreateDataSafePrivateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateDataSafePrivateEndpointDetails.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :return: The nsg_ids of this CreateDataSafePrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateDataSafePrivateEndpointDetails.
        The OCIDs of the network security groups that the private endpoint belongs to.


        :param nsg_ids: The nsg_ids of this CreateDataSafePrivateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateDataSafePrivateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateDataSafePrivateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateDataSafePrivateEndpointDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateDataSafePrivateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateDataSafePrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateDataSafePrivateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateDataSafePrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateDataSafePrivateEndpointDetails.
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
