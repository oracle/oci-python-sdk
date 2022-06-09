# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseToolsPrivateEndpoint(object):
    """
    Description of Database Tools private endpoint.
    """

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsPrivateEndpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsPrivateEndpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsPrivateEndpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsPrivateEndpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsPrivateEndpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a DatabaseToolsPrivateEndpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseToolsPrivateEndpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this DatabaseToolsPrivateEndpoint.
        :type compartment_id: str

        :param defined_tags:
            The value to assign to the defined_tags property of this DatabaseToolsPrivateEndpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param freeform_tags:
            The value to assign to the freeform_tags property of this DatabaseToolsPrivateEndpoint.
        :type freeform_tags: dict(str, str)

        :param system_tags:
            The value to assign to the system_tags property of this DatabaseToolsPrivateEndpoint.
        :type system_tags: dict(str, dict(str, object))

        :param display_name:
            The value to assign to the display_name property of this DatabaseToolsPrivateEndpoint.
        :type display_name: str

        :param description:
            The value to assign to the description property of this DatabaseToolsPrivateEndpoint.
        :type description: str

        :param id:
            The value to assign to the id property of this DatabaseToolsPrivateEndpoint.
        :type id: str

        :param endpoint_service_id:
            The value to assign to the endpoint_service_id property of this DatabaseToolsPrivateEndpoint.
        :type endpoint_service_id: str

        :param time_created:
            The value to assign to the time_created property of this DatabaseToolsPrivateEndpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this DatabaseToolsPrivateEndpoint.
        :type time_updated: datetime

        :param vcn_id:
            The value to assign to the vcn_id property of this DatabaseToolsPrivateEndpoint.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this DatabaseToolsPrivateEndpoint.
        :type subnet_id: str

        :param private_endpoint_vnic_id:
            The value to assign to the private_endpoint_vnic_id property of this DatabaseToolsPrivateEndpoint.
        :type private_endpoint_vnic_id: str

        :param private_endpoint_ip:
            The value to assign to the private_endpoint_ip property of this DatabaseToolsPrivateEndpoint.
        :type private_endpoint_ip: str

        :param endpoint_fqdn:
            The value to assign to the endpoint_fqdn property of this DatabaseToolsPrivateEndpoint.
        :type endpoint_fqdn: str

        :param additional_fqdns:
            The value to assign to the additional_fqdns property of this DatabaseToolsPrivateEndpoint.
        :type additional_fqdns: list[str]

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this DatabaseToolsPrivateEndpoint.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this DatabaseToolsPrivateEndpoint.
        :type lifecycle_details: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this DatabaseToolsPrivateEndpoint.
        :type nsg_ids: list[str]

        :param reverse_connection_configuration:
            The value to assign to the reverse_connection_configuration property of this DatabaseToolsPrivateEndpoint.
        :type reverse_connection_configuration: oci.database_tools.models.DatabaseToolsPrivateEndpointReverseConnectionConfiguration

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'defined_tags': 'dict(str, dict(str, object))',
            'freeform_tags': 'dict(str, str)',
            'system_tags': 'dict(str, dict(str, object))',
            'display_name': 'str',
            'description': 'str',
            'id': 'str',
            'endpoint_service_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'vcn_id': 'str',
            'subnet_id': 'str',
            'private_endpoint_vnic_id': 'str',
            'private_endpoint_ip': 'str',
            'endpoint_fqdn': 'str',
            'additional_fqdns': 'list[str]',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'nsg_ids': 'list[str]',
            'reverse_connection_configuration': 'DatabaseToolsPrivateEndpointReverseConnectionConfiguration'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'defined_tags': 'definedTags',
            'freeform_tags': 'freeformTags',
            'system_tags': 'systemTags',
            'display_name': 'displayName',
            'description': 'description',
            'id': 'id',
            'endpoint_service_id': 'endpointServiceId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'private_endpoint_vnic_id': 'privateEndpointVnicId',
            'private_endpoint_ip': 'privateEndpointIp',
            'endpoint_fqdn': 'endpointFqdn',
            'additional_fqdns': 'additionalFqdns',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'nsg_ids': 'nsgIds',
            'reverse_connection_configuration': 'reverseConnectionConfiguration'
        }

        self._compartment_id = None
        self._defined_tags = None
        self._freeform_tags = None
        self._system_tags = None
        self._display_name = None
        self._description = None
        self._id = None
        self._endpoint_service_id = None
        self._time_created = None
        self._time_updated = None
        self._vcn_id = None
        self._subnet_id = None
        self._private_endpoint_vnic_id = None
        self._private_endpoint_ip = None
        self._endpoint_fqdn = None
        self._additional_fqdns = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._nsg_ids = None
        self._reverse_connection_configuration = None

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the compartment containing the Database Tools private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the compartment containing the Database Tools private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this DatabaseToolsPrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this DatabaseToolsPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this DatabaseToolsPrivateEndpoint.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this DatabaseToolsPrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this DatabaseToolsPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this DatabaseToolsPrivateEndpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this DatabaseToolsPrivateEndpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this DatabaseToolsPrivateEndpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this DatabaseToolsPrivateEndpoint.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this DatabaseToolsPrivateEndpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this DatabaseToolsPrivateEndpoint.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this DatabaseToolsPrivateEndpoint.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def display_name(self):
        """
        Gets the display_name of this DatabaseToolsPrivateEndpoint.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this DatabaseToolsPrivateEndpoint.
        A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this DatabaseToolsPrivateEndpoint.
        A description of the Database Tools private endpoint.


        :return: The description of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this DatabaseToolsPrivateEndpoint.
        A description of the Database Tools private endpoint.


        :param description: The description of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._description = description

    @property
    def id(self):
        """
        **[Required]** Gets the id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the Database Tools private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the Database Tools private endpoint.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._id = id

    @property
    def endpoint_service_id(self):
        """
        **[Required]** Gets the endpoint_service_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the Database Tools Endpoint Service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The endpoint_service_id of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._endpoint_service_id

    @endpoint_service_id.setter
    def endpoint_service_id(self, endpoint_service_id):
        """
        Sets the endpoint_service_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the Database Tools Endpoint Service.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param endpoint_service_id: The endpoint_service_id of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._endpoint_service_id = endpoint_service_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this DatabaseToolsPrivateEndpoint.
        The time the Database Tools private endpoint was created. An RFC3339 formatted datetime string


        :return: The time_created of this DatabaseToolsPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this DatabaseToolsPrivateEndpoint.
        The time the Database Tools private endpoint was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this DatabaseToolsPrivateEndpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this DatabaseToolsPrivateEndpoint.
        The time the Database Tools private endpoint was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this DatabaseToolsPrivateEndpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this DatabaseToolsPrivateEndpoint.
        The time the Database Tools private endpoint was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this DatabaseToolsPrivateEndpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the VCN that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The vcn_id of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the VCN that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param vcn_id: The vcn_id of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the subnet that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The subnet_id of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the subnet that the private endpoint belongs to.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param subnet_id: The subnet_id of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def private_endpoint_vnic_id(self):
        """
        Gets the private_endpoint_vnic_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the private endpoint's VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The private_endpoint_vnic_id of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._private_endpoint_vnic_id

    @private_endpoint_vnic_id.setter
    def private_endpoint_vnic_id(self, private_endpoint_vnic_id):
        """
        Sets the private_endpoint_vnic_id of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the private endpoint's VNIC.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param private_endpoint_vnic_id: The private_endpoint_vnic_id of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._private_endpoint_vnic_id = private_endpoint_vnic_id

    @property
    def private_endpoint_ip(self):
        """
        Gets the private_endpoint_ip of this DatabaseToolsPrivateEndpoint.
        The private IP address that represents the access point for the associated endpoint service.


        :return: The private_endpoint_ip of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._private_endpoint_ip

    @private_endpoint_ip.setter
    def private_endpoint_ip(self, private_endpoint_ip):
        """
        Sets the private_endpoint_ip of this DatabaseToolsPrivateEndpoint.
        The private IP address that represents the access point for the associated endpoint service.


        :param private_endpoint_ip: The private_endpoint_ip of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._private_endpoint_ip = private_endpoint_ip

    @property
    def endpoint_fqdn(self):
        """
        Gets the endpoint_fqdn of this DatabaseToolsPrivateEndpoint.
        Then FQDN to use for the private endpoint.


        :return: The endpoint_fqdn of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._endpoint_fqdn

    @endpoint_fqdn.setter
    def endpoint_fqdn(self, endpoint_fqdn):
        """
        Sets the endpoint_fqdn of this DatabaseToolsPrivateEndpoint.
        Then FQDN to use for the private endpoint.


        :param endpoint_fqdn: The endpoint_fqdn of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._endpoint_fqdn = endpoint_fqdn

    @property
    def additional_fqdns(self):
        """
        Gets the additional_fqdns of this DatabaseToolsPrivateEndpoint.
        A list of additional FQDNs that can be also be used for the private endpoint.


        :return: The additional_fqdns of this DatabaseToolsPrivateEndpoint.
        :rtype: list[str]
        """
        return self._additional_fqdns

    @additional_fqdns.setter
    def additional_fqdns(self, additional_fqdns):
        """
        Sets the additional_fqdns of this DatabaseToolsPrivateEndpoint.
        A list of additional FQDNs that can be also be used for the private endpoint.


        :param additional_fqdns: The additional_fqdns of this DatabaseToolsPrivateEndpoint.
        :type: list[str]
        """
        self._additional_fqdns = additional_fqdns

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this DatabaseToolsPrivateEndpoint.
        The current state of the Database Tools private endpoint.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this DatabaseToolsPrivateEndpoint.
        The current state of the Database Tools private endpoint.


        :param lifecycle_state: The lifecycle_state of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this DatabaseToolsPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this DatabaseToolsPrivateEndpoint.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this DatabaseToolsPrivateEndpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this DatabaseToolsPrivateEndpoint.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the network security groups
        that the private endpoint's VNIC belongs to.  For more information about NSGs, see
        :class:`NetworkSecurityGroup`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The nsg_ids of this DatabaseToolsPrivateEndpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this DatabaseToolsPrivateEndpoint.
        The `OCID`__ of the network security groups
        that the private endpoint's VNIC belongs to.  For more information about NSGs, see
        :class:`NetworkSecurityGroup`.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param nsg_ids: The nsg_ids of this DatabaseToolsPrivateEndpoint.
        :type: list[str]
        """
        self._nsg_ids = nsg_ids

    @property
    def reverse_connection_configuration(self):
        """
        Gets the reverse_connection_configuration of this DatabaseToolsPrivateEndpoint.

        :return: The reverse_connection_configuration of this DatabaseToolsPrivateEndpoint.
        :rtype: oci.database_tools.models.DatabaseToolsPrivateEndpointReverseConnectionConfiguration
        """
        return self._reverse_connection_configuration

    @reverse_connection_configuration.setter
    def reverse_connection_configuration(self, reverse_connection_configuration):
        """
        Sets the reverse_connection_configuration of this DatabaseToolsPrivateEndpoint.

        :param reverse_connection_configuration: The reverse_connection_configuration of this DatabaseToolsPrivateEndpoint.
        :type: oci.database_tools.models.DatabaseToolsPrivateEndpointReverseConnectionConfiguration
        """
        self._reverse_connection_configuration = reverse_connection_configuration

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
