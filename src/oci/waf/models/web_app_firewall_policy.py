# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class WebAppFirewallPolicy(object):
    """
    The details of WebAppFirewallPolicy. A policy is comprised of rules, which allows executing inspections of
    incoming/outgoing HTTP message parameters and execution of actions, based on results of rules execution.

    In policy, rules are grouped into modules by their functionality. Modules can be further divided by the type
    of HTTP messages they handle:
    Modules that inspect incoming HTTP request. These modules are executed in the order they are enumerated here:
    * requestAccessControl
    * requestRateLimiting
    * requestProtection

    Modules that inspect outgoing HTTP responses. These modules are executed in the order they are enumerated here:
    * responseAccessControl
    * responseProtection
    """

    #: A constant which can be used with the lifecycle_state property of a WebAppFirewallPolicy.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a WebAppFirewallPolicy.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a WebAppFirewallPolicy.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a WebAppFirewallPolicy.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a WebAppFirewallPolicy.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a WebAppFirewallPolicy.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new WebAppFirewallPolicy object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this WebAppFirewallPolicy.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this WebAppFirewallPolicy.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this WebAppFirewallPolicy.
        :type compartment_id: str

        :param time_created:
            The value to assign to the time_created property of this WebAppFirewallPolicy.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this WebAppFirewallPolicy.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this WebAppFirewallPolicy.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this WebAppFirewallPolicy.
        :type lifecycle_details: str

        :param actions:
            The value to assign to the actions property of this WebAppFirewallPolicy.
        :type actions: list[oci.waf.models.Action]

        :param request_access_control:
            The value to assign to the request_access_control property of this WebAppFirewallPolicy.
        :type request_access_control: oci.waf.models.RequestAccessControl

        :param request_rate_limiting:
            The value to assign to the request_rate_limiting property of this WebAppFirewallPolicy.
        :type request_rate_limiting: oci.waf.models.RequestRateLimiting

        :param request_protection:
            The value to assign to the request_protection property of this WebAppFirewallPolicy.
        :type request_protection: oci.waf.models.RequestProtection

        :param response_access_control:
            The value to assign to the response_access_control property of this WebAppFirewallPolicy.
        :type response_access_control: oci.waf.models.ResponseAccessControl

        :param response_protection:
            The value to assign to the response_protection property of this WebAppFirewallPolicy.
        :type response_protection: oci.waf.models.ResponseProtection

        :param freeform_tags:
            The value to assign to the freeform_tags property of this WebAppFirewallPolicy.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this WebAppFirewallPolicy.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this WebAppFirewallPolicy.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'actions': 'list[Action]',
            'request_access_control': 'RequestAccessControl',
            'request_rate_limiting': 'RequestRateLimiting',
            'request_protection': 'RequestProtection',
            'response_access_control': 'ResponseAccessControl',
            'response_protection': 'ResponseProtection',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'actions': 'actions',
            'request_access_control': 'requestAccessControl',
            'request_rate_limiting': 'requestRateLimiting',
            'request_protection': 'requestProtection',
            'response_access_control': 'responseAccessControl',
            'response_protection': 'responseProtection',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._actions = None
        self._request_access_control = None
        self._request_rate_limiting = None
        self._request_protection = None
        self._response_access_control = None
        self._response_protection = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this WebAppFirewallPolicy.
        The `OCID`__ of the WebAppFirewallPolicy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this WebAppFirewallPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this WebAppFirewallPolicy.
        The `OCID`__ of the WebAppFirewallPolicy.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this WebAppFirewallPolicy.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this WebAppFirewallPolicy.
        WebAppFirewallPolicy display name, can be renamed.


        :return: The display_name of this WebAppFirewallPolicy.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this WebAppFirewallPolicy.
        WebAppFirewallPolicy display name, can be renamed.


        :param display_name: The display_name of this WebAppFirewallPolicy.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this WebAppFirewallPolicy.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this WebAppFirewallPolicy.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this WebAppFirewallPolicy.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this WebAppFirewallPolicy.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this WebAppFirewallPolicy.
        The time the WebAppFirewallPolicy was created. An RFC3339 formatted datetime string.


        :return: The time_created of this WebAppFirewallPolicy.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this WebAppFirewallPolicy.
        The time the WebAppFirewallPolicy was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this WebAppFirewallPolicy.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this WebAppFirewallPolicy.
        The time the WebAppFirewallPolicy was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this WebAppFirewallPolicy.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this WebAppFirewallPolicy.
        The time the WebAppFirewallPolicy was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this WebAppFirewallPolicy.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this WebAppFirewallPolicy.
        The current state of the WebAppFirewallPolicy.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this WebAppFirewallPolicy.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this WebAppFirewallPolicy.
        The current state of the WebAppFirewallPolicy.


        :param lifecycle_state: The lifecycle_state of this WebAppFirewallPolicy.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this WebAppFirewallPolicy.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in FAILED state.


        :return: The lifecycle_details of this WebAppFirewallPolicy.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this WebAppFirewallPolicy.
        A message describing the current state in more detail.
        For example, can be used to provide actionable information for a resource in FAILED state.


        :param lifecycle_details: The lifecycle_details of this WebAppFirewallPolicy.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def actions(self):
        """
        Gets the actions of this WebAppFirewallPolicy.
        Predefined actions for use in multiple different rules. Not all actions are supported in every module.
        Some actions terminate further execution of modules and rules in a module and some do not.
        Actions names must be unique within this array.


        :return: The actions of this WebAppFirewallPolicy.
        :rtype: list[oci.waf.models.Action]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """
        Sets the actions of this WebAppFirewallPolicy.
        Predefined actions for use in multiple different rules. Not all actions are supported in every module.
        Some actions terminate further execution of modules and rules in a module and some do not.
        Actions names must be unique within this array.


        :param actions: The actions of this WebAppFirewallPolicy.
        :type: list[oci.waf.models.Action]
        """
        self._actions = actions

    @property
    def request_access_control(self):
        """
        Gets the request_access_control of this WebAppFirewallPolicy.

        :return: The request_access_control of this WebAppFirewallPolicy.
        :rtype: oci.waf.models.RequestAccessControl
        """
        return self._request_access_control

    @request_access_control.setter
    def request_access_control(self, request_access_control):
        """
        Sets the request_access_control of this WebAppFirewallPolicy.

        :param request_access_control: The request_access_control of this WebAppFirewallPolicy.
        :type: oci.waf.models.RequestAccessControl
        """
        self._request_access_control = request_access_control

    @property
    def request_rate_limiting(self):
        """
        Gets the request_rate_limiting of this WebAppFirewallPolicy.

        :return: The request_rate_limiting of this WebAppFirewallPolicy.
        :rtype: oci.waf.models.RequestRateLimiting
        """
        return self._request_rate_limiting

    @request_rate_limiting.setter
    def request_rate_limiting(self, request_rate_limiting):
        """
        Sets the request_rate_limiting of this WebAppFirewallPolicy.

        :param request_rate_limiting: The request_rate_limiting of this WebAppFirewallPolicy.
        :type: oci.waf.models.RequestRateLimiting
        """
        self._request_rate_limiting = request_rate_limiting

    @property
    def request_protection(self):
        """
        Gets the request_protection of this WebAppFirewallPolicy.

        :return: The request_protection of this WebAppFirewallPolicy.
        :rtype: oci.waf.models.RequestProtection
        """
        return self._request_protection

    @request_protection.setter
    def request_protection(self, request_protection):
        """
        Sets the request_protection of this WebAppFirewallPolicy.

        :param request_protection: The request_protection of this WebAppFirewallPolicy.
        :type: oci.waf.models.RequestProtection
        """
        self._request_protection = request_protection

    @property
    def response_access_control(self):
        """
        Gets the response_access_control of this WebAppFirewallPolicy.

        :return: The response_access_control of this WebAppFirewallPolicy.
        :rtype: oci.waf.models.ResponseAccessControl
        """
        return self._response_access_control

    @response_access_control.setter
    def response_access_control(self, response_access_control):
        """
        Sets the response_access_control of this WebAppFirewallPolicy.

        :param response_access_control: The response_access_control of this WebAppFirewallPolicy.
        :type: oci.waf.models.ResponseAccessControl
        """
        self._response_access_control = response_access_control

    @property
    def response_protection(self):
        """
        Gets the response_protection of this WebAppFirewallPolicy.

        :return: The response_protection of this WebAppFirewallPolicy.
        :rtype: oci.waf.models.ResponseProtection
        """
        return self._response_protection

    @response_protection.setter
    def response_protection(self, response_protection):
        """
        Sets the response_protection of this WebAppFirewallPolicy.

        :param response_protection: The response_protection of this WebAppFirewallPolicy.
        :type: oci.waf.models.ResponseProtection
        """
        self._response_protection = response_protection

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this WebAppFirewallPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this WebAppFirewallPolicy.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this WebAppFirewallPolicy.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this WebAppFirewallPolicy.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this WebAppFirewallPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this WebAppFirewallPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this WebAppFirewallPolicy.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this WebAppFirewallPolicy.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        **[Required]** Gets the system_tags of this WebAppFirewallPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this WebAppFirewallPolicy.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this WebAppFirewallPolicy.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this WebAppFirewallPolicy.
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
