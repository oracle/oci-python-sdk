# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAiPrivateEndpointDetails(object):
    """
    Information about the new private endpoint resource.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAiPrivateEndpointDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param dns_zones:
            The value to assign to the dns_zones property of this CreateAiPrivateEndpointDetails.
        :type dns_zones: list[str]

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateAiPrivateEndpointDetails.
        :type subnet_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateAiPrivateEndpointDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAiPrivateEndpointDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAiPrivateEndpointDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this CreateAiPrivateEndpointDetails.
        :type display_name: str

        """
        self.swagger_types = {
            'dns_zones': 'list[str]',
            'subnet_id': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'display_name': 'str'
        }

        self.attribute_map = {
            'dns_zones': 'dnsZones',
            'subnet_id': 'subnetId',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'display_name': 'displayName'
        }

        self._dns_zones = None
        self._subnet_id = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._display_name = None

    @property
    def dns_zones(self):
        """
        **[Required]** Gets the dns_zones of this CreateAiPrivateEndpointDetails.
        List of DNS zones to be used by the data assets.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :return: The dns_zones of this CreateAiPrivateEndpointDetails.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this CreateAiPrivateEndpointDetails.
        List of DNS zones to be used by the data assets.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :param dns_zones: The dns_zones of this CreateAiPrivateEndpointDetails.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this CreateAiPrivateEndpointDetails.
        The OCID of subnet to which the reverse connection is to be created.


        :return: The subnet_id of this CreateAiPrivateEndpointDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateAiPrivateEndpointDetails.
        The OCID of subnet to which the reverse connection is to be created.


        :param subnet_id: The subnet_id of this CreateAiPrivateEndpointDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateAiPrivateEndpointDetails.
        Compartment identifier.


        :return: The compartment_id of this CreateAiPrivateEndpointDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateAiPrivateEndpointDetails.
        Compartment identifier.


        :param compartment_id: The compartment_id of this CreateAiPrivateEndpointDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAiPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateAiPrivateEndpointDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAiPrivateEndpointDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateAiPrivateEndpointDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAiPrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateAiPrivateEndpointDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAiPrivateEndpointDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateAiPrivateEndpointDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this CreateAiPrivateEndpointDetails.
        Display name of the private endpoint resource being created.


        :return: The display_name of this CreateAiPrivateEndpointDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateAiPrivateEndpointDetails.
        Display name of the private endpoint resource being created.


        :param display_name: The display_name of this CreateAiPrivateEndpointDetails.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
