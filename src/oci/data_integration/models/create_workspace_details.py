# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateWorkspaceDetails(object):
    """
    The information needed to create a new workspace.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateWorkspaceDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this CreateWorkspaceDetails.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateWorkspaceDetails.
        :type subnet_id: str

        :param dns_server_ip:
            The value to assign to the dns_server_ip property of this CreateWorkspaceDetails.
        :type dns_server_ip: str

        :param dns_server_zone:
            The value to assign to the dns_server_zone property of this CreateWorkspaceDetails.
        :type dns_server_zone: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateWorkspaceDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateWorkspaceDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this CreateWorkspaceDetails.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this CreateWorkspaceDetails.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateWorkspaceDetails.
        :type compartment_id: str

        :param is_private_network_enabled:
            The value to assign to the is_private_network_enabled property of this CreateWorkspaceDetails.
        :type is_private_network_enabled: bool

        :param registry_id:
            The value to assign to the registry_id property of this CreateWorkspaceDetails.
        :type registry_id: str

        :param endpoint_id:
            The value to assign to the endpoint_id property of this CreateWorkspaceDetails.
        :type endpoint_id: str

        :param registry_name:
            The value to assign to the registry_name property of this CreateWorkspaceDetails.
        :type registry_name: str

        :param registry_compartment_id:
            The value to assign to the registry_compartment_id property of this CreateWorkspaceDetails.
        :type registry_compartment_id: str

        :param endpoint_name:
            The value to assign to the endpoint_name property of this CreateWorkspaceDetails.
        :type endpoint_name: str

        :param endpoint_compartment_id:
            The value to assign to the endpoint_compartment_id property of this CreateWorkspaceDetails.
        :type endpoint_compartment_id: str

        """
        self.swagger_types = {
            'vcn_id': 'str',
            'subnet_id': 'str',
            'dns_server_ip': 'str',
            'dns_server_zone': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'description': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'is_private_network_enabled': 'bool',
            'registry_id': 'str',
            'endpoint_id': 'str',
            'registry_name': 'str',
            'registry_compartment_id': 'str',
            'endpoint_name': 'str',
            'endpoint_compartment_id': 'str'
        }

        self.attribute_map = {
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'dns_server_ip': 'dnsServerIp',
            'dns_server_zone': 'dnsServerZone',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'description': 'description',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'is_private_network_enabled': 'isPrivateNetworkEnabled',
            'registry_id': 'registryId',
            'endpoint_id': 'endpointId',
            'registry_name': 'registryName',
            'registry_compartment_id': 'registryCompartmentId',
            'endpoint_name': 'endpointName',
            'endpoint_compartment_id': 'endpointCompartmentId'
        }

        self._vcn_id = None
        self._subnet_id = None
        self._dns_server_ip = None
        self._dns_server_zone = None
        self._freeform_tags = None
        self._defined_tags = None
        self._description = None
        self._display_name = None
        self._compartment_id = None
        self._is_private_network_enabled = None
        self._registry_id = None
        self._endpoint_id = None
        self._registry_name = None
        self._registry_compartment_id = None
        self._endpoint_name = None
        self._endpoint_compartment_id = None

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this CreateWorkspaceDetails.
        The OCID of the VCN the subnet is in.


        :return: The vcn_id of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this CreateWorkspaceDetails.
        The OCID of the VCN the subnet is in.


        :param vcn_id: The vcn_id of this CreateWorkspaceDetails.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this CreateWorkspaceDetails.
        The OCID of the subnet for customer connected databases.


        :return: The subnet_id of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this CreateWorkspaceDetails.
        The OCID of the subnet for customer connected databases.


        :param subnet_id: The subnet_id of this CreateWorkspaceDetails.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def dns_server_ip(self):
        """
        Gets the dns_server_ip of this CreateWorkspaceDetails.
        The IP of the custom DNS.


        :return: The dns_server_ip of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._dns_server_ip

    @dns_server_ip.setter
    def dns_server_ip(self, dns_server_ip):
        """
        Sets the dns_server_ip of this CreateWorkspaceDetails.
        The IP of the custom DNS.


        :param dns_server_ip: The dns_server_ip of this CreateWorkspaceDetails.
        :type: str
        """
        self._dns_server_ip = dns_server_ip

    @property
    def dns_server_zone(self):
        """
        Gets the dns_server_zone of this CreateWorkspaceDetails.
        The DNS zone of the custom DNS to use to resolve names.


        :return: The dns_server_zone of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._dns_server_zone

    @dns_server_zone.setter
    def dns_server_zone(self, dns_server_zone):
        """
        Sets the dns_server_zone of this CreateWorkspaceDetails.
        The DNS zone of the custom DNS to use to resolve names.


        :param dns_server_zone: The dns_server_zone of this CreateWorkspaceDetails.
        :type: str
        """
        self._dns_server_zone = dns_server_zone

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateWorkspaceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this CreateWorkspaceDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateWorkspaceDetails.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this CreateWorkspaceDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateWorkspaceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this CreateWorkspaceDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateWorkspaceDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this CreateWorkspaceDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this CreateWorkspaceDetails.
        A user defined description for the workspace.


        :return: The description of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this CreateWorkspaceDetails.
        A user defined description for the workspace.


        :param description: The description of this CreateWorkspaceDetails.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this CreateWorkspaceDetails.
        A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.


        :return: The display_name of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this CreateWorkspaceDetails.
        A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this CreateWorkspaceDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this CreateWorkspaceDetails.
        The OCID of the compartment containing the workspace.


        :return: The compartment_id of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this CreateWorkspaceDetails.
        The OCID of the compartment containing the workspace.


        :param compartment_id: The compartment_id of this CreateWorkspaceDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def is_private_network_enabled(self):
        """
        Gets the is_private_network_enabled of this CreateWorkspaceDetails.
        Specifies whether the private network connection is enabled or disabled.


        :return: The is_private_network_enabled of this CreateWorkspaceDetails.
        :rtype: bool
        """
        return self._is_private_network_enabled

    @is_private_network_enabled.setter
    def is_private_network_enabled(self, is_private_network_enabled):
        """
        Sets the is_private_network_enabled of this CreateWorkspaceDetails.
        Specifies whether the private network connection is enabled or disabled.


        :param is_private_network_enabled: The is_private_network_enabled of this CreateWorkspaceDetails.
        :type: bool
        """
        self._is_private_network_enabled = is_private_network_enabled

    @property
    def registry_id(self):
        """
        Gets the registry_id of this CreateWorkspaceDetails.
        DCMS Data Asset Registry ID to which the workspace is associated


        :return: The registry_id of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        """
        Sets the registry_id of this CreateWorkspaceDetails.
        DCMS Data Asset Registry ID to which the workspace is associated


        :param registry_id: The registry_id of this CreateWorkspaceDetails.
        :type: str
        """
        self._registry_id = registry_id

    @property
    def endpoint_id(self):
        """
        Gets the endpoint_id of this CreateWorkspaceDetails.
        DCMS Private Endpoint ID associated with workspace if the pvt networking is enabled


        :return: The endpoint_id of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """
        Sets the endpoint_id of this CreateWorkspaceDetails.
        DCMS Private Endpoint ID associated with workspace if the pvt networking is enabled


        :param endpoint_id: The endpoint_id of this CreateWorkspaceDetails.
        :type: str
        """
        self._endpoint_id = endpoint_id

    @property
    def registry_name(self):
        """
        Gets the registry_name of this CreateWorkspaceDetails.
        DCMS Data Asset Registry display name


        :return: The registry_name of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        """
        Sets the registry_name of this CreateWorkspaceDetails.
        DCMS Data Asset Registry display name


        :param registry_name: The registry_name of this CreateWorkspaceDetails.
        :type: str
        """
        self._registry_name = registry_name

    @property
    def registry_compartment_id(self):
        """
        Gets the registry_compartment_id of this CreateWorkspaceDetails.
        DCMS Data Asset Registry Compartment Identifier


        :return: The registry_compartment_id of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._registry_compartment_id

    @registry_compartment_id.setter
    def registry_compartment_id(self, registry_compartment_id):
        """
        Sets the registry_compartment_id of this CreateWorkspaceDetails.
        DCMS Data Asset Registry Compartment Identifier


        :param registry_compartment_id: The registry_compartment_id of this CreateWorkspaceDetails.
        :type: str
        """
        self._registry_compartment_id = registry_compartment_id

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this CreateWorkspaceDetails.
        DCMS Private Endpoint Name


        :return: The endpoint_name of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this CreateWorkspaceDetails.
        DCMS Private Endpoint Name


        :param endpoint_name: The endpoint_name of this CreateWorkspaceDetails.
        :type: str
        """
        self._endpoint_name = endpoint_name

    @property
    def endpoint_compartment_id(self):
        """
        Gets the endpoint_compartment_id of this CreateWorkspaceDetails.
        DCMS PRivate Endpoint Compartment Identifier


        :return: The endpoint_compartment_id of this CreateWorkspaceDetails.
        :rtype: str
        """
        return self._endpoint_compartment_id

    @endpoint_compartment_id.setter
    def endpoint_compartment_id(self, endpoint_compartment_id):
        """
        Sets the endpoint_compartment_id of this CreateWorkspaceDetails.
        DCMS PRivate Endpoint Compartment Identifier


        :param endpoint_compartment_id: The endpoint_compartment_id of this CreateWorkspaceDetails.
        :type: str
        """
        self._endpoint_compartment_id = endpoint_compartment_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
