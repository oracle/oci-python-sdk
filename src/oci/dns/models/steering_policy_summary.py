# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SteeringPolicySummary(object):
    """
    A DNS steering policy.

    **Warning:** Oracle recommends that you avoid using any confidential information when you supply string values using the API.
    """

    #: A constant which can be used with the template property of a SteeringPolicySummary.
    #: This constant has a value of "FAILOVER"
    TEMPLATE_FAILOVER = "FAILOVER"

    #: A constant which can be used with the template property of a SteeringPolicySummary.
    #: This constant has a value of "LOAD_BALANCE"
    TEMPLATE_LOAD_BALANCE = "LOAD_BALANCE"

    #: A constant which can be used with the template property of a SteeringPolicySummary.
    #: This constant has a value of "ROUTE_BY_GEO"
    TEMPLATE_ROUTE_BY_GEO = "ROUTE_BY_GEO"

    #: A constant which can be used with the template property of a SteeringPolicySummary.
    #: This constant has a value of "ROUTE_BY_ASN"
    TEMPLATE_ROUTE_BY_ASN = "ROUTE_BY_ASN"

    #: A constant which can be used with the template property of a SteeringPolicySummary.
    #: This constant has a value of "ROUTE_BY_IP"
    TEMPLATE_ROUTE_BY_IP = "ROUTE_BY_IP"

    #: A constant which can be used with the template property of a SteeringPolicySummary.
    #: This constant has a value of "CUSTOM"
    TEMPLATE_CUSTOM = "CUSTOM"

    #: A constant which can be used with the lifecycle_state property of a SteeringPolicySummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SteeringPolicySummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SteeringPolicySummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SteeringPolicySummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    def __init__(self, **kwargs):
        """
        Initializes a new SteeringPolicySummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this SteeringPolicySummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this SteeringPolicySummary.
        :type display_name: str

        :param ttl:
            The value to assign to the ttl property of this SteeringPolicySummary.
        :type ttl: int

        :param health_check_monitor_id:
            The value to assign to the health_check_monitor_id property of this SteeringPolicySummary.
        :type health_check_monitor_id: str

        :param template:
            The value to assign to the template property of this SteeringPolicySummary.
            Allowed values for this property are: "FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type template: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this SteeringPolicySummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this SteeringPolicySummary.
        :type defined_tags: dict(str, dict(str, object))

        :param _self:
            The value to assign to the _self property of this SteeringPolicySummary.
        :type _self: str

        :param id:
            The value to assign to the id property of this SteeringPolicySummary.
        :type id: str

        :param time_created:
            The value to assign to the time_created property of this SteeringPolicySummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SteeringPolicySummary.
            Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'display_name': 'str',
            'ttl': 'int',
            'health_check_monitor_id': 'str',
            'template': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            '_self': 'str',
            'id': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'ttl': 'ttl',
            'health_check_monitor_id': 'healthCheckMonitorId',
            'template': 'template',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            '_self': 'self',
            'id': 'id',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._compartment_id = None
        self._display_name = None
        self._ttl = None
        self._health_check_monitor_id = None
        self._template = None
        self._freeform_tags = None
        self._defined_tags = None
        self.__self = None
        self._id = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this SteeringPolicySummary.
        The OCID of the compartment containing the steering policy.


        :return: The compartment_id of this SteeringPolicySummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this SteeringPolicySummary.
        The OCID of the compartment containing the steering policy.


        :param compartment_id: The compartment_id of this SteeringPolicySummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this SteeringPolicySummary.
        A user-friendly name for the steering policy. Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :return: The display_name of this SteeringPolicySummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SteeringPolicySummary.
        A user-friendly name for the steering policy. Does not have to be unique and can be changed.
        Avoid entering confidential information.


        :param display_name: The display_name of this SteeringPolicySummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def ttl(self):
        """
        Gets the ttl of this SteeringPolicySummary.
        The Time To Live (TTL) for responses from the steering policy, in seconds.
        If not specified during creation, a value of 30 seconds will be used.


        :return: The ttl of this SteeringPolicySummary.
        :rtype: int
        """
        return self._ttl

    @ttl.setter
    def ttl(self, ttl):
        """
        Sets the ttl of this SteeringPolicySummary.
        The Time To Live (TTL) for responses from the steering policy, in seconds.
        If not specified during creation, a value of 30 seconds will be used.


        :param ttl: The ttl of this SteeringPolicySummary.
        :type: int
        """
        self._ttl = ttl

    @property
    def health_check_monitor_id(self):
        """
        Gets the health_check_monitor_id of this SteeringPolicySummary.
        The OCID of the health check monitor providing health data about the answers of the
        steering policy. A steering policy answer with `rdata` matching a monitored endpoint
        will use the health data of that endpoint. A steering policy answer with `rdata` not
        matching any monitored endpoint will be assumed healthy.


        **Note:** To use the Health Check monitoring feature in a steering policy, a monitor
        must be created using the Health Checks service first. For more information on how to
        create a monitor, please see `Managing Health Checks`__.

        __ https://docs.cloud.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm


        :return: The health_check_monitor_id of this SteeringPolicySummary.
        :rtype: str
        """
        return self._health_check_monitor_id

    @health_check_monitor_id.setter
    def health_check_monitor_id(self, health_check_monitor_id):
        """
        Sets the health_check_monitor_id of this SteeringPolicySummary.
        The OCID of the health check monitor providing health data about the answers of the
        steering policy. A steering policy answer with `rdata` matching a monitored endpoint
        will use the health data of that endpoint. A steering policy answer with `rdata` not
        matching any monitored endpoint will be assumed healthy.


        **Note:** To use the Health Check monitoring feature in a steering policy, a monitor
        must be created using the Health Checks service first. For more information on how to
        create a monitor, please see `Managing Health Checks`__.

        __ https://docs.cloud.oracle.com/iaas/Content/HealthChecks/Tasks/managinghealthchecks.htm


        :param health_check_monitor_id: The health_check_monitor_id of this SteeringPolicySummary.
        :type: str
        """
        self._health_check_monitor_id = health_check_monitor_id

    @property
    def template(self):
        """
        Gets the template of this SteeringPolicySummary.
        A set of predefined rules based on the desired purpose of the steering policy. Each
        template utilizes Traffic Management's rules in a different order to produce the desired
        results when answering DNS queries.


        **Example:** The `FAILOVER` template determines answers by filtering the policy's answers
        using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`,
        and `LIMIT`. This gives the domain dynamic failover capability.


        It is **strongly recommended** to use a template other than `CUSTOM` when creating
        a steering policy.


        All templates require the rule order to begin with an unconditional `FILTER` rule that keeps
        answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined
        `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`.
        The last rule of a template must must be a `LIMIT` rule. For more information about templates
        and code examples, see `Traffic Management API Guide`__.

        **Template Types**

        * `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers
        to serve. If an endpoint fails a health check, the answer for that endpoint will be removed
        from the list of available answers until the endpoint is detected as healthy.


        * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights.


        * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic
        locations to route by, see `Traffic Management Geographic Locations`__.


        * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN.


        * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address.


        * `CUSTOM` - Allows a customized configuration of rules.

        __ https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm
        __ https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm

        Allowed values for this property are: "FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The template of this SteeringPolicySummary.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this SteeringPolicySummary.
        A set of predefined rules based on the desired purpose of the steering policy. Each
        template utilizes Traffic Management's rules in a different order to produce the desired
        results when answering DNS queries.


        **Example:** The `FAILOVER` template determines answers by filtering the policy's answers
        using the `FILTER` rule first, then the following rules in succession: `HEALTH`, `PRIORITY`,
        and `LIMIT`. This gives the domain dynamic failover capability.


        It is **strongly recommended** to use a template other than `CUSTOM` when creating
        a steering policy.


        All templates require the rule order to begin with an unconditional `FILTER` rule that keeps
        answers contingent upon `answer.isDisabled != true`, except for `CUSTOM`. A defined
        `HEALTH` rule must follow the `FILTER` rule if the policy references a `healthCheckMonitorId`.
        The last rule of a template must must be a `LIMIT` rule. For more information about templates
        and code examples, see `Traffic Management API Guide`__.

        **Template Types**

        * `FAILOVER` - Uses health check information on your endpoints to determine which DNS answers
        to serve. If an endpoint fails a health check, the answer for that endpoint will be removed
        from the list of available answers until the endpoint is detected as healthy.


        * `LOAD_BALANCE` - Distributes web traffic to specified endpoints based on defined weights.


        * `ROUTE_BY_GEO` - Answers DNS queries based on the query's geographic location. For a list of geographic
        locations to route by, see `Traffic Management Geographic Locations`__.


        * `ROUTE_BY_ASN` - Answers DNS queries based on the query's originating ASN.


        * `ROUTE_BY_IP` - Answers DNS queries based on the query's IP address.


        * `CUSTOM` - Allows a customized configuration of rules.

        __ https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Concepts/trafficmanagementapi.htm
        __ https://docs.cloud.oracle.com/iaas/Content/TrafficManagement/Reference/trafficmanagementgeo.htm


        :param template: The template of this SteeringPolicySummary.
        :type: str
        """
        allowed_values = ["FAILOVER", "LOAD_BALANCE", "ROUTE_BY_GEO", "ROUTE_BY_ASN", "ROUTE_BY_IP", "CUSTOM"]
        if not value_allowed_none_or_none_sentinel(template, allowed_values):
            template = 'UNKNOWN_ENUM_VALUE'
        self._template = template

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this SteeringPolicySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this SteeringPolicySummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this SteeringPolicySummary.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this SteeringPolicySummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this SteeringPolicySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this SteeringPolicySummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this SteeringPolicySummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        For more information, see `Resource Tags`__.


        **Example:** `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this SteeringPolicySummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def _self(self):
        """
        Gets the _self of this SteeringPolicySummary.
        The canonical absolute URL of the resource.


        :return: The _self of this SteeringPolicySummary.
        :rtype: str
        """
        return self.__self

    @_self.setter
    def _self(self, _self):
        """
        Sets the _self of this SteeringPolicySummary.
        The canonical absolute URL of the resource.


        :param _self: The _self of this SteeringPolicySummary.
        :type: str
        """
        self.__self = _self

    @property
    def id(self):
        """
        Gets the id of this SteeringPolicySummary.
        The OCID of the resource.


        :return: The id of this SteeringPolicySummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this SteeringPolicySummary.
        The OCID of the resource.


        :param id: The id of this SteeringPolicySummary.
        :type: str
        """
        self._id = id

    @property
    def time_created(self):
        """
        Gets the time_created of this SteeringPolicySummary.
        The date and time the resource was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :return: The time_created of this SteeringPolicySummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this SteeringPolicySummary.
        The date and time the resource was created, expressed in RFC 3339 timestamp format.

        **Example:** `2016-07-22T17:23:59:60Z`


        :param time_created: The time_created of this SteeringPolicySummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this SteeringPolicySummary.
        The current state of the resource.

        Allowed values for this property are: "ACTIVE", "CREATING", "DELETED", "DELETING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SteeringPolicySummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SteeringPolicySummary.
        The current state of the resource.


        :param lifecycle_state: The lifecycle_state of this SteeringPolicySummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "DELETED", "DELETING"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
