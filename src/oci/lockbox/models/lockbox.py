# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Lockbox(object):
    """
    Description of Lockbox.
    """

    #: A constant which can be used with the lockbox_partner property of a Lockbox.
    #: This constant has a value of "FAAAS"
    LOCKBOX_PARTNER_FAAAS = "FAAAS"

    #: A constant which can be used with the lockbox_partner property of a Lockbox.
    #: This constant has a value of "CANARY"
    LOCKBOX_PARTNER_CANARY = "CANARY"

    #: A constant which can be used with the lifecycle_state property of a Lockbox.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a Lockbox.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a Lockbox.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a Lockbox.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a Lockbox.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a Lockbox.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new Lockbox object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this Lockbox.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this Lockbox.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Lockbox.
        :type compartment_id: str

        :param partner_compartment_id:
            The value to assign to the partner_compartment_id property of this Lockbox.
        :type partner_compartment_id: str

        :param resource_id:
            The value to assign to the resource_id property of this Lockbox.
        :type resource_id: str

        :param lockbox_partner:
            The value to assign to the lockbox_partner property of this Lockbox.
            Allowed values for this property are: "FAAAS", "CANARY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lockbox_partner: str

        :param time_created:
            The value to assign to the time_created property of this Lockbox.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this Lockbox.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this Lockbox.
            Allowed values for this property are: "ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param access_context_attributes:
            The value to assign to the access_context_attributes property of this Lockbox.
        :type access_context_attributes: oci.lockbox.models.AccessContextAttributeCollection

        :param approval_template_id:
            The value to assign to the approval_template_id property of this Lockbox.
        :type approval_template_id: str

        :param max_access_duration:
            The value to assign to the max_access_duration property of this Lockbox.
        :type max_access_duration: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this Lockbox.
        :type lifecycle_details: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Lockbox.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Lockbox.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this Lockbox.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'partner_compartment_id': 'str',
            'resource_id': 'str',
            'lockbox_partner': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'access_context_attributes': 'AccessContextAttributeCollection',
            'approval_template_id': 'str',
            'max_access_duration': 'str',
            'lifecycle_details': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'partner_compartment_id': 'partnerCompartmentId',
            'resource_id': 'resourceId',
            'lockbox_partner': 'lockboxPartner',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'access_context_attributes': 'accessContextAttributes',
            'approval_template_id': 'approvalTemplateId',
            'max_access_duration': 'maxAccessDuration',
            'lifecycle_details': 'lifecycleDetails',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._partner_compartment_id = None
        self._resource_id = None
        self._lockbox_partner = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._access_context_attributes = None
        self._approval_template_id = None
        self._max_access_duration = None
        self._lifecycle_details = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this Lockbox.
        Unique identifier that is immutable on creation


        :return: The id of this Lockbox.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this Lockbox.
        Unique identifier that is immutable on creation


        :param id: The id of this Lockbox.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this Lockbox.
        Lockbox Identifier, can be renamed


        :return: The display_name of this Lockbox.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this Lockbox.
        Lockbox Identifier, can be renamed


        :param display_name: The display_name of this Lockbox.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this Lockbox.
        Compartment Identifier


        :return: The compartment_id of this Lockbox.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Lockbox.
        Compartment Identifier


        :param compartment_id: The compartment_id of this Lockbox.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def partner_compartment_id(self):
        """
        **[Required]** Gets the partner_compartment_id of this Lockbox.
        Compartment Identifier


        :return: The partner_compartment_id of this Lockbox.
        :rtype: str
        """
        return self._partner_compartment_id

    @partner_compartment_id.setter
    def partner_compartment_id(self, partner_compartment_id):
        """
        Sets the partner_compartment_id of this Lockbox.
        Compartment Identifier


        :param partner_compartment_id: The partner_compartment_id of this Lockbox.
        :type: str
        """
        self._partner_compartment_id = partner_compartment_id

    @property
    def resource_id(self):
        """
        **[Required]** Gets the resource_id of this Lockbox.
        The unique identifier (OCID) of associated resource that the lockbox is created for.


        :return: The resource_id of this Lockbox.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this Lockbox.
        The unique identifier (OCID) of associated resource that the lockbox is created for.


        :param resource_id: The resource_id of this Lockbox.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def lockbox_partner(self):
        """
        **[Required]** Gets the lockbox_partner of this Lockbox.
        The partner using this lockbox to lock a resource.

        Allowed values for this property are: "FAAAS", "CANARY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lockbox_partner of this Lockbox.
        :rtype: str
        """
        return self._lockbox_partner

    @lockbox_partner.setter
    def lockbox_partner(self, lockbox_partner):
        """
        Sets the lockbox_partner of this Lockbox.
        The partner using this lockbox to lock a resource.


        :param lockbox_partner: The lockbox_partner of this Lockbox.
        :type: str
        """
        allowed_values = ["FAAAS", "CANARY"]
        if not value_allowed_none_or_none_sentinel(lockbox_partner, allowed_values):
            lockbox_partner = 'UNKNOWN_ENUM_VALUE'
        self._lockbox_partner = lockbox_partner

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this Lockbox.
        The time the the Lockbox was created. An RFC3339 formatted datetime string


        :return: The time_created of this Lockbox.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this Lockbox.
        The time the the Lockbox was created. An RFC3339 formatted datetime string


        :param time_created: The time_created of this Lockbox.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this Lockbox.
        The time the Lockbox was updated. An RFC3339 formatted datetime string


        :return: The time_updated of this Lockbox.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this Lockbox.
        The time the Lockbox was updated. An RFC3339 formatted datetime string


        :param time_updated: The time_updated of this Lockbox.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this Lockbox.
        The current state of the Lockbox.

        Allowed values for this property are: "ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this Lockbox.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this Lockbox.
        The current state of the Lockbox.


        :param lifecycle_state: The lifecycle_state of this Lockbox.
        :type: str
        """
        allowed_values = ["ACTIVE", "CREATING", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def access_context_attributes(self):
        """
        Gets the access_context_attributes of this Lockbox.

        :return: The access_context_attributes of this Lockbox.
        :rtype: oci.lockbox.models.AccessContextAttributeCollection
        """
        return self._access_context_attributes

    @access_context_attributes.setter
    def access_context_attributes(self, access_context_attributes):
        """
        Sets the access_context_attributes of this Lockbox.

        :param access_context_attributes: The access_context_attributes of this Lockbox.
        :type: oci.lockbox.models.AccessContextAttributeCollection
        """
        self._access_context_attributes = access_context_attributes

    @property
    def approval_template_id(self):
        """
        Gets the approval_template_id of this Lockbox.
        Approval template ID


        :return: The approval_template_id of this Lockbox.
        :rtype: str
        """
        return self._approval_template_id

    @approval_template_id.setter
    def approval_template_id(self, approval_template_id):
        """
        Sets the approval_template_id of this Lockbox.
        Approval template ID


        :param approval_template_id: The approval_template_id of this Lockbox.
        :type: str
        """
        self._approval_template_id = approval_template_id

    @property
    def max_access_duration(self):
        """
        Gets the max_access_duration of this Lockbox.
        The maximum amount of time operator has access to associated resources.


        :return: The max_access_duration of this Lockbox.
        :rtype: str
        """
        return self._max_access_duration

    @max_access_duration.setter
    def max_access_duration(self, max_access_duration):
        """
        Sets the max_access_duration of this Lockbox.
        The maximum amount of time operator has access to associated resources.


        :param max_access_duration: The max_access_duration of this Lockbox.
        :type: str
        """
        self._max_access_duration = max_access_duration

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this Lockbox.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this Lockbox.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this Lockbox.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this Lockbox.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this Lockbox.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this Lockbox.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Lockbox.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this Lockbox.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this Lockbox.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this Lockbox.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Lockbox.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this Lockbox.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this Lockbox.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this Lockbox.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this Lockbox.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this Lockbox.
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
