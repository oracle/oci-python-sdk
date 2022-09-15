# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Workspace(object):
    """
    A workspace is an organizational construct to keep multiple data integration solutions and their resources (data assets, data flows, tasks, and so on) separate from each other, helping you to stay organized. For example, you could have separate workspaces for development, testing, and production.
    """

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "STARTING"
    LIFECYCLE_STATE_STARTING = "STARTING"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "STOPPING"
    LIFECYCLE_STATE_STOPPING = "STOPPING"

    #: A constant which can be used with the lifecycle_state property of a Workspace.
    #: This constant has a value of "STOPPED"
    LIFECYCLE_STATE_STOPPED = "STOPPED"

    def __init__(self, **kwargs):
        """
        Initializes a new Workspace object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param vcn_id:
            The value to assign to the vcn_id property of this Workspace.
        :type vcn_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this Workspace.
        :type subnet_id: str

        :param dns_server_ip:
            The value to assign to the dns_server_ip property of this Workspace.
        :type dns_server_ip: str

        :param dns_server_zone:
            The value to assign to the dns_server_zone property of this Workspace.
        :type dns_server_zone: str

        :param is_private_network_enabled:
            The value to assign to the is_private_network_enabled property of this Workspace.
        :type is_private_network_enabled: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Workspace.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Workspace.
        :type defined_tags: dict(str, dict(str, object))

        :param description:
            The value to assign to the description property of this Workspace.
        :type description: str

        :param display_name:
            The value to assign to the display_name property of this Workspace.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Workspace.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this Workspace.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Workspace.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Workspace.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param state_message:
            The value to assign to the state_message property of this Workspace.
        :type state_message: str

        :param id:
            The value to assign to the id property of this Workspace.
        :type id: str

        :param endpoint_id:
            The value to assign to the endpoint_id property of this Workspace.
        :type endpoint_id: str

        :param endpoint_name:
            The value to assign to the endpoint_name property of this Workspace.
        :type endpoint_name: str

        :param registry_id:
            The value to assign to the registry_id property of this Workspace.
        :type registry_id: str

        """
        self.swagger_types = {
            'vcn_id': 'str',
            'subnet_id': 'str',
            'dns_server_ip': 'str',
            'dns_server_zone': 'str',
            'is_private_network_enabled': 'bool',
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
            'endpoint_id': 'str',
            'endpoint_name': 'str',
            'registry_id': 'str'
        }

        self.attribute_map = {
            'vcn_id': 'vcnId',
            'subnet_id': 'subnetId',
            'dns_server_ip': 'dnsServerIp',
            'dns_server_zone': 'dnsServerZone',
            'is_private_network_enabled': 'isPrivateNetworkEnabled',
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
            'endpoint_id': 'endpointId',
            'endpoint_name': 'endpointName',
            'registry_id': 'registryId'
        }

        self._vcn_id = None
        self._subnet_id = None
        self._dns_server_ip = None
        self._dns_server_zone = None
        self._is_private_network_enabled = None
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
        self._endpoint_id = None
        self._endpoint_name = None
        self._registry_id = None

    @property
    def vcn_id(self):
        """
        Gets the vcn_id of this Workspace.
        The OCID of the VCN the subnet is in.


        :return: The vcn_id of this Workspace.
        :rtype: str
        """
        return self._vcn_id

    @vcn_id.setter
    def vcn_id(self, vcn_id):
        """
        Sets the vcn_id of this Workspace.
        The OCID of the VCN the subnet is in.


        :param vcn_id: The vcn_id of this Workspace.
        :type: str
        """
        self._vcn_id = vcn_id

    @property
    def subnet_id(self):
        """
        Gets the subnet_id of this Workspace.
        The OCID of the subnet for customer connected databases.


        :return: The subnet_id of this Workspace.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """
        Sets the subnet_id of this Workspace.
        The OCID of the subnet for customer connected databases.


        :param subnet_id: The subnet_id of this Workspace.
        :type: str
        """
        self._subnet_id = subnet_id

    @property
    def dns_server_ip(self):
        """
        Gets the dns_server_ip of this Workspace.
        The IP of the custom DNS.


        :return: The dns_server_ip of this Workspace.
        :rtype: str
        """
        return self._dns_server_ip

    @dns_server_ip.setter
    def dns_server_ip(self, dns_server_ip):
        """
        Sets the dns_server_ip of this Workspace.
        The IP of the custom DNS.


        :param dns_server_ip: The dns_server_ip of this Workspace.
        :type: str
        """
        self._dns_server_ip = dns_server_ip

    @property
    def dns_server_zone(self):
        """
        Gets the dns_server_zone of this Workspace.
        The DNS zone of the custom DNS to use to resolve names.


        :return: The dns_server_zone of this Workspace.
        :rtype: str
        """
        return self._dns_server_zone

    @dns_server_zone.setter
    def dns_server_zone(self, dns_server_zone):
        """
        Sets the dns_server_zone of this Workspace.
        The DNS zone of the custom DNS to use to resolve names.


        :param dns_server_zone: The dns_server_zone of this Workspace.
        :type: str
        """
        self._dns_server_zone = dns_server_zone

    @property
    def is_private_network_enabled(self):
        """
        Gets the is_private_network_enabled of this Workspace.
        Specifies whether the private network connection is enabled or disabled.


        :return: The is_private_network_enabled of this Workspace.
        :rtype: bool
        """
        return self._is_private_network_enabled

    @is_private_network_enabled.setter
    def is_private_network_enabled(self, is_private_network_enabled):
        """
        Sets the is_private_network_enabled of this Workspace.
        Specifies whether the private network connection is enabled or disabled.


        :param is_private_network_enabled: The is_private_network_enabled of this Workspace.
        :type: bool
        """
        self._is_private_network_enabled = is_private_network_enabled

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Workspace.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Workspace.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Workspace.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See `Resource Tags`__.
        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Workspace.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Workspace.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Workspace.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Workspace.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. See `Resource Tags`__.
        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Workspace.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def description(self):
        """
        Gets the description of this Workspace.
        A detailed description for the workspace.


        :return: The description of this Workspace.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Workspace.
        A detailed description for the workspace.


        :param description: The description of this Workspace.
        :type: str
        """
        self._description = description

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Workspace.
        A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.


        :return: The display_name of this Workspace.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Workspace.
        A user-friendly display name for the workspace. Does not have to be unique, and can be modified. Avoid entering confidential information.


        :param display_name: The display_name of this Workspace.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Workspace.
        The OCID of the compartment containing the workspace.


        :return: The compartment_id of this Workspace.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Workspace.
        The OCID of the compartment containing the workspace.


        :param compartment_id: The compartment_id of this Workspace.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        Gets the time_created of this Workspace.
        The date and time the workspace was created, in the timestamp format defined by RFC3339.


        :return: The time_created of this Workspace.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Workspace.
        The date and time the workspace was created, in the timestamp format defined by RFC3339.


        :param time_created: The time_created of this Workspace.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Workspace.
        The date and time the workspace was updated, in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this Workspace.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Workspace.
        The date and time the workspace was updated, in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this Workspace.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this Workspace.
        Lifecycle states for workspaces in Data Integration Service
        CREATING - The resource is being created and may not be usable until the entire metadata is defined
        UPDATING - The resource is being updated and may not be usable until all changes are commited
        DELETING - The resource is being deleted and might require deep cleanup of children.
        ACTIVE   - The resource is valid and available for access
        INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                 administrative reasons
        DELETED  - The resource has been deleted and isn't available
        FAILED   - The resource is in a failed state due to validation or other errors
        STARTING - The resource is being started and may not be usable until becomes ACTIVE again
        STOPPING - The resource is in the process of Stopping and may not be usable until it Stops or fails
        STOPPED  - The resource is in Stopped state due to stop operation.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Workspace.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Workspace.
        Lifecycle states for workspaces in Data Integration Service
        CREATING - The resource is being created and may not be usable until the entire metadata is defined
        UPDATING - The resource is being updated and may not be usable until all changes are commited
        DELETING - The resource is being deleted and might require deep cleanup of children.
        ACTIVE   - The resource is valid and available for access
        INACTIVE - The resource might be incomplete in its definition or might have been made unavailable for
                 administrative reasons
        DELETED  - The resource has been deleted and isn't available
        FAILED   - The resource is in a failed state due to validation or other errors
        STARTING - The resource is being started and may not be usable until becomes ACTIVE again
        STOPPING - The resource is in the process of Stopping and may not be usable until it Stops or fails
        STOPPED  - The resource is in Stopped state due to stop operation.


        :param lifecycle_state: The lifecycle_state of this Workspace.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "STARTING", "STOPPING", "STOPPED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def state_message(self):
        """
        Gets the state_message of this Workspace.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.


        :return: The state_message of this Workspace.
        :rtype: str
        """
        return self._state_message

    @state_message.setter
    def state_message(self, state_message):
        """
        Sets the state_message of this Workspace.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in failed state.


        :param state_message: The state_message of this Workspace.
        :type: str
        """
        self._state_message = state_message

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Workspace.
        A system-generated and immutable identifier assigned to the workspace upon creation.


        :return: The id of this Workspace.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Workspace.
        A system-generated and immutable identifier assigned to the workspace upon creation.


        :param id: The id of this Workspace.
        :type: str
        """
        self._id = id

    @property
    def endpoint_id(self):
        """
        Gets the endpoint_id of this Workspace.
        OCID of the private endpoint associated with the container/workspace.


        :return: The endpoint_id of this Workspace.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        """
        Sets the endpoint_id of this Workspace.
        OCID of the private endpoint associated with the container/workspace.


        :param endpoint_id: The endpoint_id of this Workspace.
        :type: str
        """
        self._endpoint_id = endpoint_id

    @property
    def endpoint_name(self):
        """
        Gets the endpoint_name of this Workspace.
        Name of the private endpoint associated with the container/workspace.


        :return: The endpoint_name of this Workspace.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        """
        Sets the endpoint_name of this Workspace.
        Name of the private endpoint associated with the container/workspace.


        :param endpoint_name: The endpoint_name of this Workspace.
        :type: str
        """
        self._endpoint_name = endpoint_name

    @property
    def registry_id(self):
        """
        Gets the registry_id of this Workspace.
        DCMS Registry ID associated with the container/workspace.


        :return: The registry_id of this Workspace.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        """
        Sets the registry_id of this Workspace.
        DCMS Registry ID associated with the container/workspace.


        :param registry_id: The registry_id of this Workspace.
        :type: str
        """
        self._registry_id = registry_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
