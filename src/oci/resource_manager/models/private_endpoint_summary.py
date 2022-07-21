# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PrivateEndpointSummary(object):
    """
    The summary metadata associated with the private endpoint.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new PrivateEndpointSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this PrivateEndpointSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this PrivateEndpointSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this PrivateEndpointSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this PrivateEndpointSummary.
        :type description: str

        :param vcn_id:
            The value to assign to the vcn_id property of this PrivateEndpointSummary.
        :type vcn_id: str

        :param is_used_with_configuration_source_provider:
            The value to assign to the is_used_with_configuration_source_provider property of this PrivateEndpointSummary.
        :type is_used_with_configuration_source_provider: bool

        :param dns_zones:
            The value to assign to the dns_zones property of this PrivateEndpointSummary.
        :type dns_zones: list[str]

        :param time_created:
            The value to assign to the time_created property of this PrivateEndpointSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PrivateEndpointSummary.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this PrivateEndpointSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this PrivateEndpointSummary.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'vcn_id': 'str',
            'is_used_with_configuration_source_provider': 'bool',
            'dns_zones': 'list[str]',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'vcn_id': 'vcnId',
            'is_used_with_configuration_source_provider': 'isUsedWithConfigurationSourceProvider',
            'dns_zones': 'dnsZones',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._vcn_id = None
        self._is_used_with_configuration_source_provider = None
        self._dns_zones = None
        self._time_created = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this PrivateEndpointSummary.
        The `OCID`__ of the private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this PrivateEndpointSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this PrivateEndpointSummary.
        The `OCID`__ of the private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this PrivateEndpointSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this PrivateEndpointSummary.
        The `OCID`__ of the compartment containing this private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this PrivateEndpointSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this PrivateEndpointSummary.
        The `OCID`__ of the compartment containing this private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this PrivateEndpointSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this PrivateEndpointSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this PrivateEndpointSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this PrivateEndpointSummary.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this PrivateEndpointSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this PrivateEndpointSummary.
        Description of the private endpoint. Avoid entering confidential information.


        :return: The description of this PrivateEndpointSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this PrivateEndpointSummary.
        Description of the private endpoint. Avoid entering confidential information.


        :param description: The description of this PrivateEndpointSummary.
        :type: str
        """
        self._description = description

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this PrivateEndpointSummary.
        The `OCID`__ of the VCN for the private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this PrivateEndpointSummary.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this PrivateEndpointSummary.
        The `OCID`__ of the VCN for the private endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this PrivateEndpointSummary.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def is_used_with_configuration_source_provider(self):
        """
        Gets the is_used_with_configuration_source_provider of this PrivateEndpointSummary.
        When `true`, allows the private endpoint to be used with a configuration source provider.


        :return: The is_used_with_configuration_source_provider of this PrivateEndpointSummary.
        :rtype: bool
        """
        return self._is_used_with_configuration_source_provider

    @is_used_with_configuration_source_provider.setter
    def is_used_with_configuration_source_provider(self, is_used_with_configuration_source_provider):
        """
        Sets the is_used_with_configuration_source_provider of this PrivateEndpointSummary.
        When `true`, allows the private endpoint to be used with a configuration source provider.


        :param is_used_with_configuration_source_provider: The is_used_with_configuration_source_provider of this PrivateEndpointSummary.
        :type: bool
        """
        self._is_used_with_configuration_source_provider = is_used_with_configuration_source_provider

    @property
    def dns_zones(self):
        """
        Gets the dns_zones of this PrivateEndpointSummary.
        DNS zones to use for accessing private Git servers.
        For private Git server instructions, see
        `Private Git Server`__.
        DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to service provider VCN resolver.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git


        :return: The dns_zones of this PrivateEndpointSummary.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this PrivateEndpointSummary.
        DNS zones to use for accessing private Git servers.
        For private Git server instructions, see
        `Private Git Server`__.
        DNS Proxy forwards any DNS FQDN queries over into the consumer DNS resolver if the DNS FQDN is included in the dns zones list otherwise it goes to service provider VCN resolver.

        __ https://docs.cloud.oracle.com/iaas/Content/ResourceManager/Tasks/private-endpoints.htm#private-git


        :param dns_zones: The dns_zones of this PrivateEndpointSummary.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def time_created(self):
        """
        Gets the time_created of this PrivateEndpointSummary.
        The date and time when the private endpoint was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :return: The time_created of this PrivateEndpointSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this PrivateEndpointSummary.
        The date and time when the private endpoint was created.
        Format is defined by RFC3339.
        Example: `2020-01-25T21:10:29.600Z`


        :param time_created: The time_created of this PrivateEndpointSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this PrivateEndpointSummary.
        The current lifecycle state of the private endpoint.
        Allowable values:
        - ACTIVE
        - CREATING
        - DELETING
        - DELETED
        - FAILED


        :return: The lifecycle_state of this PrivateEndpointSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PrivateEndpointSummary.
        The current lifecycle state of the private endpoint.
        Allowable values:
        - ACTIVE
        - CREATING
        - DELETING
        - DELETED
        - FAILED


        :param lifecycle_state: The lifecycle_state of this PrivateEndpointSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this PrivateEndpointSummary.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this PrivateEndpointSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this PrivateEndpointSummary.
        Free-form tags associated with the resource. Each tag is a key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this PrivateEndpointSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this PrivateEndpointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this PrivateEndpointSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this PrivateEndpointSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this PrivateEndpointSummary.
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
