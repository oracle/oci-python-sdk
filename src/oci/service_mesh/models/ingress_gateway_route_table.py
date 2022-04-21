# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngressGatewayRouteTable(object):
    """
    This resource represents a customer-managed ingress gateway route table in the Service Mesh.
    """

    #: A constant which can be used with the lifecycle_state property of a IngressGatewayRouteTable.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a IngressGatewayRouteTable.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a IngressGatewayRouteTable.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a IngressGatewayRouteTable.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a IngressGatewayRouteTable.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a IngressGatewayRouteTable.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new IngressGatewayRouteTable object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this IngressGatewayRouteTable.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this IngressGatewayRouteTable.
        :type compartment_id: str

        :param ingress_gateway_id:
            The value to assign to the ingress_gateway_id property of this IngressGatewayRouteTable.
        :type ingress_gateway_id: str

        :param name:
            The value to assign to the name property of this IngressGatewayRouteTable.
        :type name: str

        :param description:
            The value to assign to the description property of this IngressGatewayRouteTable.
        :type description: str

        :param priority:
            The value to assign to the priority property of this IngressGatewayRouteTable.
        :type priority: int

        :param route_rules:
            The value to assign to the route_rules property of this IngressGatewayRouteTable.
        :type route_rules: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]

        :param time_created:
            The value to assign to the time_created property of this IngressGatewayRouteTable.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this IngressGatewayRouteTable.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this IngressGatewayRouteTable.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this IngressGatewayRouteTable.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this IngressGatewayRouteTable.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this IngressGatewayRouteTable.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this IngressGatewayRouteTable.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'ingress_gateway_id': 'str',
            'name': 'str',
            'description': 'str',
            'priority': 'int',
            'route_rules': 'list[IngressGatewayTrafficRouteRule]',
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
            'ingress_gateway_id': 'ingressGatewayId',
            'name': 'name',
            'description': 'description',
            'priority': 'priority',
            'route_rules': 'routeRules',
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
        self._ingress_gateway_id = None
        self._name = None
        self._description = None
        self._priority = None
        self._route_rules = None
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
        **[Required]** Gets the id of this IngressGatewayRouteTable.
        Unique identifier that is immutable on creation.


        :return: The id of this IngressGatewayRouteTable.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this IngressGatewayRouteTable.
        Unique identifier that is immutable on creation.


        :param id: The id of this IngressGatewayRouteTable.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this IngressGatewayRouteTable.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this IngressGatewayRouteTable.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this IngressGatewayRouteTable.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this IngressGatewayRouteTable.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def ingress_gateway_id(self):
        """
        **[Required]** Gets the ingress_gateway_id of this IngressGatewayRouteTable.
        The OCID of the ingress gateway.


        :return: The ingress_gateway_id of this IngressGatewayRouteTable.
        :rtype: str
        """
        return self._ingress_gateway_id

    @ingress_gateway_id.setter
    def ingress_gateway_id(self, ingress_gateway_id):
        """
        Sets the ingress_gateway_id of this IngressGatewayRouteTable.
        The OCID of the ingress gateway.


        :param ingress_gateway_id: The ingress_gateway_id of this IngressGatewayRouteTable.
        :type: str
        """
        self._ingress_gateway_id = ingress_gateway_id

    @property
    def name(self):
        """
        **[Required]** Gets the name of this IngressGatewayRouteTable.
        A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :return: The name of this IngressGatewayRouteTable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this IngressGatewayRouteTable.
        A user-friendly name. The name must be unique within the same ingress gateway and cannot be changed after creation.
        Avoid entering confidential information.

        Example: `My unique resource name`


        :param name: The name of this IngressGatewayRouteTable.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this IngressGatewayRouteTable.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :return: The description of this IngressGatewayRouteTable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this IngressGatewayRouteTable.
        Description of the resource. It can be changed after creation.
        Avoid entering confidential information.

        Example: `This is my new resource`


        :param description: The description of this IngressGatewayRouteTable.
        :type: str
        """
        self._description = description

    @property
    def priority(self):
        """
        Gets the priority of this IngressGatewayRouteTable.
        The priority of the route table. A lower value means a higher priority. The routes are declared based on the priority.


        :return: The priority of this IngressGatewayRouteTable.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """
        Sets the priority of this IngressGatewayRouteTable.
        The priority of the route table. A lower value means a higher priority. The routes are declared based on the priority.


        :param priority: The priority of this IngressGatewayRouteTable.
        :type: int
        """
        self._priority = priority

    @property
    def route_rules(self):
        """
        **[Required]** Gets the route_rules of this IngressGatewayRouteTable.
        The route rules for the ingress gateway.


        :return: The route_rules of this IngressGatewayRouteTable.
        :rtype: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]
        """
        return self._route_rules

    @route_rules.setter
    def route_rules(self, route_rules):
        """
        Sets the route_rules of this IngressGatewayRouteTable.
        The route rules for the ingress gateway.


        :param route_rules: The route_rules of this IngressGatewayRouteTable.
        :type: list[oci.service_mesh.models.IngressGatewayTrafficRouteRule]
        """
        self._route_rules = route_rules

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this IngressGatewayRouteTable.
        The time when this resource was created in an RFC3339 formatted datetime string.


        :return: The time_created of this IngressGatewayRouteTable.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this IngressGatewayRouteTable.
        The time when this resource was created in an RFC3339 formatted datetime string.


        :param time_created: The time_created of this IngressGatewayRouteTable.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this IngressGatewayRouteTable.
        The time when this resource was updated in an RFC3339 formatted datetime string.


        :return: The time_updated of this IngressGatewayRouteTable.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this IngressGatewayRouteTable.
        The time when this resource was updated in an RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this IngressGatewayRouteTable.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this IngressGatewayRouteTable.
        The current state of the Resource.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this IngressGatewayRouteTable.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this IngressGatewayRouteTable.
        The current state of the Resource.


        :param lifecycle_state: The lifecycle_state of this IngressGatewayRouteTable.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this IngressGatewayRouteTable.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.


        :return: The lifecycle_details of this IngressGatewayRouteTable.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this IngressGatewayRouteTable.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in a Failed state.


        :param lifecycle_details: The lifecycle_details of this IngressGatewayRouteTable.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this IngressGatewayRouteTable.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this IngressGatewayRouteTable.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this IngressGatewayRouteTable.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this IngressGatewayRouteTable.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this IngressGatewayRouteTable.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this IngressGatewayRouteTable.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this IngressGatewayRouteTable.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this IngressGatewayRouteTable.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this IngressGatewayRouteTable.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this IngressGatewayRouteTable.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this IngressGatewayRouteTable.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this IngressGatewayRouteTable.
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
