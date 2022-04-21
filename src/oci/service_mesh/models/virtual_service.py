# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualService(object):
    """
    This resource represents a customer-managed service in the Service Mesh. Each virtual service declares multiple running versions of the service and maps to a group of instances/pods running a specific version of the actual service.
    """

    #: A constant which can be used with the lifecycle_state property of a VirtualService.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a VirtualService.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a VirtualService.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a VirtualService.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a VirtualService.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a VirtualService.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualService object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this VirtualService.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this VirtualService.
        :type compartment_id: str

        :param mesh_id:
            The value to assign to the mesh_id property of this VirtualService.
        :type mesh_id: str

        :param name:
            The value to assign to the name property of this VirtualService.
        :type name: str

        :param description:
            The value to assign to the description property of this VirtualService.
        :type description: str

        :param default_routing_policy:
            The value to assign to the default_routing_policy property of this VirtualService.
        :type default_routing_policy: oci.service_mesh.models.DefaultVirtualServiceRoutingPolicy

        :param hosts:
            The value to assign to the hosts property of this VirtualService.
        :type hosts: list[str]

        :param mtls:
            The value to assign to the mtls property of this VirtualService.
        :type mtls: oci.service_mesh.models.MutualTransportLayerSecurity

        :param time_created:
            The value to assign to the time_created property of this VirtualService.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this VirtualService.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this VirtualService.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this VirtualService.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this VirtualService.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this VirtualService.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this VirtualService.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'mesh_id': 'str',
            'name': 'str',
            'description': 'str',
            'default_routing_policy': 'DefaultVirtualServiceRoutingPolicy',
            'hosts': 'list[str]',
            'mtls': 'MutualTransportLayerSecurity',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'mesh_id': 'meshId',
            'name': 'name',
            'description': 'description',
            'default_routing_policy': 'defaultRoutingPolicy',
            'hosts': 'hosts',
            'mtls': 'mtls',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._mesh_id = None
        self._name = None
        self._description = None
        self._default_routing_policy = None
        self._hosts = None
        self._mtls = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this VirtualService.
        Unique identifier that is immutable on creation.


        :return: The id of this VirtualService.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this VirtualService.
        Unique identifier that is immutable on creation.


        :param id: The id of this VirtualService.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this VirtualService.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this VirtualService.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this VirtualService.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this VirtualService.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def mesh_id(self):
        """
        **[Required]** Gets the mesh_id of this VirtualService.
        The OCID of the service mesh in which this virtual service is created.


        :return: The mesh_id of this VirtualService.
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """
        Sets the mesh_id of this VirtualService.
        The OCID of the service mesh in which this virtual service is created.


        :param mesh_id: The mesh_id of this VirtualService.
        :type: str
        """
        self._mesh_id = mesh_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this VirtualService.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :return: The name of this VirtualService.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this VirtualService.
        A user-friendly name. The name has to be unique within the same service mesh and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :param name: The name of this VirtualService.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this VirtualService.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this VirtualService.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this VirtualService.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this VirtualService.
        :type: str
        """
        self._description = description

    @property
    def default_routing_policy(self):
        """
        Gets the default_routing_policy of this VirtualService.

        :return: The default_routing_policy of this VirtualService.
        :rtype: oci.service_mesh.models.DefaultVirtualServiceRoutingPolicy
        """
        return self._default_routing_policy

    @default_routing_policy.setter
    def default_routing_policy(self, default_routing_policy):
        """
        Sets the default_routing_policy of this VirtualService.

        :param default_routing_policy: The default_routing_policy of this VirtualService.
        :type: oci.service_mesh.models.DefaultVirtualServiceRoutingPolicy
        """
        self._default_routing_policy = default_routing_policy

    @property
    def hosts(self):
        """
        Gets the hosts of this VirtualService.
        The DNS hostnames of the virtual service that is used by its callers.
        Wildcard hostnames are supported in the prefix form.
        Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\".
        Can be omitted if the virtual service will only have TCP virtual deployments.


        :return: The hosts of this VirtualService.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """
        Sets the hosts of this VirtualService.
        The DNS hostnames of the virtual service that is used by its callers.
        Wildcard hostnames are supported in the prefix form.
        Examples of valid hostnames are \"www.example.com\", \"*.example.com\", \"*.com\".
        Can be omitted if the virtual service will only have TCP virtual deployments.


        :param hosts: The hosts of this VirtualService.
        :type: list[str]
        """
        self._hosts = hosts

    @property
    def mtls(self):
        """
        Gets the mtls of this VirtualService.

        :return: The mtls of this VirtualService.
        :rtype: oci.service_mesh.models.MutualTransportLayerSecurity
        """
        return self._mtls

    @mtls.setter
    def mtls(self, mtls):
        """
        Sets the mtls of this VirtualService.

        :param mtls: The mtls of this VirtualService.
        :type: oci.service_mesh.models.MutualTransportLayerSecurity
        """
        self._mtls = mtls

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this VirtualService.
        The time when this resource was created in an RFC3339 formatted datetime string.


        :return: The time_created of this VirtualService.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this VirtualService.
        The time when this resource was created in an RFC3339 formatted datetime string.


        :param time_created: The time_created of this VirtualService.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this VirtualService.
        The time when this resource was updated in an RFC3339 formatted datetime string.


        :return: The time_updated of this VirtualService.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this VirtualService.
        The time when this resource was updated in an RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this VirtualService.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this VirtualService.
        The current state of the Resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this VirtualService.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this VirtualService.
        The current state of the Resource.


        :param lifecycle_state: The lifecycle_state of this VirtualService.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this VirtualService.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this VirtualService.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this VirtualService.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this VirtualService.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this VirtualService.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this VirtualService.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this VirtualService.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this VirtualService.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this VirtualService.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this VirtualService.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this VirtualService.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this VirtualService.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this VirtualService.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this VirtualService.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this VirtualService.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this VirtualService.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
