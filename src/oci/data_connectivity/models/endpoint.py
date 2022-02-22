# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Endpoint(object):
    """
    An Endpoint is an organizational construct to keep multiple data Connectivity Management solutions and their resources (pe-id, dnsProxyIp, dnsZones, and so on) separate from each other, helping you to stay organized. For example, you could have separate registries for development, testing, and production.
    """

    #: A constant which can be used with the lifecycle_state property of a Endpoint.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Endpoint.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Endpoint.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Endpoint.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Endpoint.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Endpoint.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Endpoint.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Endpoint object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this Endpoint.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this Endpoint.
        :type subnet_id: str

        :param dns_zones:
            The value to assign to the dns_zones property of this Endpoint.
        :type dns_zones: list[str]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Endpoint.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Endpoint.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this Endpoint.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this Endpoint.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Endpoint.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this Endpoint.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Endpoint.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Endpoint.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this Endpoint.
        :type state_message: str

        :param id:
            The value to assign to the id property of this Endpoint.
        :type id: str

        :param endpoint_size:
            The value to assign to the endpoint_size property of this Endpoint.
        :type endpoint_size: int

        :param nsg_ids:
            The value to assign to the nsg_ids property of this Endpoint.
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
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'state_message': 'str',
            'id': 'str',
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
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'state_message': 'stateMessage',
            'id': 'id',
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
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._state_message = None
        self._id = None
        self._endpoint_size = None
        self._nsg_ids = None

    @property
    def vcn_id(self):
        """
        **[Required]** Gets the vcn_id of this Endpoint.
        VCN OCID where the subnet resides.


        :return: The vcn_id of this Endpoint.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this Endpoint.
        VCN OCID where the subnet resides.


        :param vcn_id: The vcn_id of this Endpoint.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        **[Required]** Gets the subnet_id of this Endpoint.
        Subnet OCID for the customer connected network where databases for example reside.


        :return: The subnet_id of this Endpoint.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Endpoint.
        Subnet OCID for the customer connected network where databases for example reside.


        :param subnet_id: The subnet_id of this Endpoint.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def dns_zones(self):
        """
        Gets the dns_zones of this Endpoint.
        List of DNS zones to be used by the data assets to be harvested.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :return: The dns_zones of this Endpoint.
        :rtype: list[str]
        """
        return self._dns_zones

    @dns_zones.setter
    def dns_zones(self, dns_zones):
        """
        Sets the dns_zones of this Endpoint.
        List of DNS zones to be used by the data assets to be harvested.
        Example: custpvtsubnet.oraclevcn.com for data asset: db.custpvtsubnet.oraclevcn.com


        :param dns_zones: The dns_zones of this Endpoint.
        :type: list[str]
        """
        self._dns_zones = dns_zones

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Endpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Endpoint.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Endpoint.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Endpoint.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Endpoint.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Endpoint.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Endpoint.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Endpoint.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this Endpoint.
        Registry description


        :return: The description of this Endpoint.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Endpoint.
        Registry description


        :param description: The description of this Endpoint.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Endpoint.
        Data Connectivity Management Registry display name, registries can be renamed


        :return: The display_name of this Endpoint.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Endpoint.
        Data Connectivity Management Registry display name, registries can be renamed


        :param display_name: The display_name of this Endpoint.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Endpoint.
        Compartment Identifier


        :return: The compartment_id of this Endpoint.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Endpoint.
        Compartment Identifier


        :param compartment_id: The compartment_id of this Endpoint.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Endpoint.
        The time the Data Connectivity Management Registry was created. An RFC3339 formatted datetime string


        :return: The time_created of this Endpoint.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Endpoint.
        The time the Data Connectivity Management Registry was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this Endpoint.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Endpoint.
        The time the Data Connectivity Management Registry was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this Endpoint.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Endpoint.
        The time the Data Connectivity Management Registry was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this Endpoint.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Endpoint.
        Lifecycle states for registries in Data Connectivity Management Service
        CREATING - The resource is being created and may not be usable until the entire metadata is defined
        UPDATING - The resource is being updated and may not be usable until all changes are commited
        DELETING - The resource is being deleted and might require deep cleanup of children.
        ACTIVE   - The resource is valid and available for access
        INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                 administrative reasons
        DELETED  - The resource has been deleted and isn't available
        FAILED   - The resource is in a failed state due to validation or other errors

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Endpoint.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Endpoint.
        Lifecycle states for registries in Data Connectivity Management Service
        CREATING - The resource is being created and may not be usable until the entire metadata is defined
        UPDATING - The resource is being updated and may not be usable until all changes are commited
        DELETING - The resource is being deleted and might require deep cleanup of children.
        ACTIVE   - The resource is valid and available for access
        INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                 administrative reasons
        DELETED  - The resource has been deleted and isn't available
        FAILED   - The resource is in a failed state due to validation or other errors


        :param lifecycle_state: The lifecycle_state of this Endpoint.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this Endpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The state_message of this Endpoint.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this Endpoint.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param state_message: The state_message of this Endpoint.
        :type: str
        """
        self._state_message = state_message

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Endpoint.
        Unique identifier that is immutable on creation


        :return: The id of this Endpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Endpoint.
        Unique identifier that is immutable on creation


        :param id: The id of this Endpoint.
        :type: str
        """
        self._id = id

    @property
    def endpoint_size(self):
        """
        Gets the endpoint_size of this Endpoint.
        Endpoint size for reverse connection capacity.


        :return: The endpoint_size of this Endpoint.
        :rtype: int
        """
        return self._endpoint_size

    @endpoint_size.setter
    def endpoint_size(self, endpoint_size):
        """
        Sets the endpoint_size of this Endpoint.
        Endpoint size for reverse connection capacity.


        :param endpoint_size: The endpoint_size of this Endpoint.
        :type: int
        """
        self._endpoint_size = endpoint_size

    @property
    def nsg_ids(self):
        """
        Gets the nsg_ids of this Endpoint.
        List of NSGs to which the Private Endpoint VNIC must be added.


        :return: The nsg_ids of this Endpoint.
        :rtype: list[str]
        """
        return self._nsg_ids

    @nsg_ids.setter
    def nsg_ids(self, nsg_ids):
        """
        Sets the nsg_ids of this Endpoint.
        List of NSGs to which the Private Endpoint VNIC must be added.


        :param nsg_ids: The nsg_ids of this Endpoint.
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
