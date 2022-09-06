# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateEndpointDetails(object):
    """
    Information about a new endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateEndpointDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateEndpointDetails.
        :type subnet_id: str

        :param dns_zones:
            The value to assign to the dns_zones property of this CreateEndpointDetails.
        :type dns_zones: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this CreateEndpointDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateEndpointDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateEndpointDetails.
        :type compartment_id: str

        :param endpoint_size:
            The value to assign to the endpoint_size property of this CreateEndpointDetails.
        :type endpoint_size: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateEndpointDetails.
        :type nsg_ids: list[str]

        """
        self.swagger_types = {
            'vcn_id': 'str',
            'subnet_id': 'str',
            'dns_zones': 'list[str]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'endpoint_size': 'int',
            'nsg_ids': 'list[str]'
        }

        self.attribute_map = {
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'dns_zones': 'dnsZones',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'endpoint_size': 'endpointSize',
            'nsg_ids': 'nsgIds'
        }

        self._vcn_id = None
        self._subnet_id = None
        self._dns_zones = None
        self._freeform_tags = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._compartment_id = None
        self._endpoint_size = None
        self._nsg_ids = None

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateEndpointDetails.
        VCN identifier where the subnet resides.


        :return: The vcn_id of this CreateEndpointDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateEndpointDetails.
        VCN identifier where the subnet resides.


        :param vcn_id: The vcn_id of this CreateEndpointDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateEndpointDetails.
        Subnet identifier for the customer-connected databases.


        :return: The subnet_id of this CreateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateEndpointDetails.
        Subnet identifier for the customer-connected databases.


        :param subnet_id: The subnet_id of this CreateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def dns_zones(self):
        """
        Gets the dns_zones of this CreateEndpointDetails.
        The list of DNS zones to be used by the data assets to be harvested.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :return: The dns_zones of this CreateEndpointDetails.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this CreateEndpointDetails.
        The list of DNS zones to be used by the data assets to be harvested.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :param dns_zones: The dns_zones of this CreateEndpointDetails.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope. Exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateEndpointDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateEndpointDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this CreateEndpointDetails.
        Data Connectivity Management Registry description


        :return: The description of this CreateEndpointDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateEndpointDetails.
        Data Connectivity Management Registry description


        :param description: The description of this CreateEndpointDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateEndpointDetails.
        The Data Connectivity Management registry display name; registries can be renamed.


        :return: The display_name of this CreateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateEndpointDetails.
        The Data Connectivity Management registry display name; registries can be renamed.


        :param display_name: The display_name of this CreateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this CreateEndpointDetails.
        Compartment Identifier


        :return: The compartment_id of this CreateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateEndpointDetails.
        Compartment Identifier


        :param compartment_id: The compartment_id of this CreateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def endpoint_size(self):
        """
        Gets the endpoint_size of this CreateEndpointDetails.
        Endpoint size for reverse connection capacity.


        :return: The endpoint_size of this CreateEndpointDetails.
        :rtype: int
        """
        return self._endpoint_size

    @endpoint_size.setter
    def endpoint_size(self, endpoint_size):
        """
        Sets the endpoint_size of this CreateEndpointDetails.
        Endpoint size for reverse connection capacity.


        :param endpoint_size: The endpoint_size of this CreateEndpointDetails.
        :type: int
        """
        self._endpoint_size = endpoint_size

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this CreateEndpointDetails.
        The list of NSGs to which the private endpoint VNIC must be added.


        :return: The nsg_ids of this CreateEndpointDetails.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this CreateEndpointDetails.
        The list of NSGs to which the private endpoint VNIC must be added.


        :param nsg_ids: The nsg_ids of this CreateEndpointDetails.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
