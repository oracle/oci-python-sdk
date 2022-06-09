# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class GovernanceRule(object):
    """
    Represents a rule in parent tenancy which governs resources in child tenancies.
    """

    #: A constant which can be used with the type property of a GovernanceRule.
    #: This constant has a value of "QUOTA"
    TYPE_QUOTA = "QUOTA"

    #: A constant which can be used with the type property of a GovernanceRule.
    #: This constant has a value of "TAG"
    TYPE_TAG = "TAG"

    #: A constant which can be used with the type property of a GovernanceRule.
    #: This constant has a value of "ALLOWED_REGIONS"
    TYPE_ALLOWED_REGIONS = "ALLOWED_REGIONS"

    #: A constant which can be used with the creation_option property of a GovernanceRule.
    #: This constant has a value of "TEMPLATE"
    CREATION_OPTION_TEMPLATE = "TEMPLATE"

    #: A constant which can be used with the creation_option property of a GovernanceRule.
    #: This constant has a value of "CLONE"
    CREATION_OPTION_CLONE = "CLONE"

    #: A constant which can be used with the lifecycle_state property of a GovernanceRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a GovernanceRule.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new GovernanceRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this GovernanceRule.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this GovernanceRule.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this GovernanceRule.
        :type display_name: str

        :param description:
            The value to assign to the description property of this GovernanceRule.
        :type description: str

        :param type:
            The value to assign to the type property of this GovernanceRule.
            Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param creation_option:
            The value to assign to the creation_option property of this GovernanceRule.
            Allowed values for this property are: "TEMPLATE", "CLONE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type creation_option: str

        :param template:
            The value to assign to the template property of this GovernanceRule.
        :type template: oci.governance_rules_control_plane.models.Template

        :param related_resource_id:
            The value to assign to the related_resource_id property of this GovernanceRule.
        :type related_resource_id: str

        :param time_created:
            The value to assign to the time_created property of this GovernanceRule.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this GovernanceRule.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this GovernanceRule.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this GovernanceRule.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this GovernanceRule.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this GovernanceRule.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'creation_option': 'str',
            'template': 'Template',
            'related_resource_id': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'creation_option': 'creationOption',
            'template': 'template',
            'related_resource_id': 'relatedResourceId',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._type = None
        self._creation_option = None
        self._template = None
        self._related_resource_id = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this GovernanceRule.
        The Oracle ID (`OCID`__) of the governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this GovernanceRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this GovernanceRule.
        The Oracle ID (`OCID`__) of the governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this GovernanceRule.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this GovernanceRule.
        The Oracle ID (`OCID`__) of the root compartment containing the governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this GovernanceRule.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this GovernanceRule.
        The Oracle ID (`OCID`__) of the root compartment containing the governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this GovernanceRule.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this GovernanceRule.
        Display name of the governance rule.


        :return: The display_name of this GovernanceRule.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this GovernanceRule.
        Display name of the governance rule.


        :param display_name: The display_name of this GovernanceRule.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this GovernanceRule.
        Description of the governance rule.


        :return: The description of this GovernanceRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this GovernanceRule.
        Description of the governance rule.


        :param description: The description of this GovernanceRule.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this GovernanceRule.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`

        Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this GovernanceRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this GovernanceRule.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`


        :param type: The type of this GovernanceRule.
        :type: str
        """
        allowed_values = ["QUOTA", "TAG", "ALLOWED_REGIONS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def creation_option(self):
        """
        **[Required]** Gets the creation_option of this GovernanceRule.
        The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

        Example: `TEMPLATE`

        Allowed values for this property are: "TEMPLATE", "CLONE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The creation_option of this GovernanceRule.
        :rtype: str
        """
        return self._creation_option

    @creation_option.setter
    def creation_option(self, creation_option):
        """
        Sets the creation_option of this GovernanceRule.
        The type of option used to create the governance rule, could be one of TEMPLATE or CLONE.

        Example: `TEMPLATE`


        :param creation_option: The creation_option of this GovernanceRule.
        :type: str
        """
        allowed_values = ["TEMPLATE", "CLONE"]
        if not value_allowed_none_or_none_sentinel(creation_option, allowed_values):
            creation_option = 'UNKNOWN_ENUM_VALUE'
        self._creation_option = creation_option

    @property
    def template(self):
        """
        **[Required]** Gets the template of this GovernanceRule.

        :return: The template of this GovernanceRule.
        :rtype: oci.governance_rules_control_plane.models.Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this GovernanceRule.

        :param template: The template of this GovernanceRule.
        :type: oci.governance_rules_control_plane.models.Template
        """
        self._template = template

    @property
    def related_resource_id(self):
        """
        Gets the related_resource_id of this GovernanceRule.
        The Oracle ID (`OCID`__) of the resource, which was used as a template to create this governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The related_resource_id of this GovernanceRule.
        :rtype: str
        """
        return self._related_resource_id

    @related_resource_id.setter
    def related_resource_id(self, related_resource_id):
        """
        Sets the related_resource_id of this GovernanceRule.
        The Oracle ID (`OCID`__) of the resource, which was used as a template to create this governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param related_resource_id: The related_resource_id of this GovernanceRule.
        :type: str
        """
        self._related_resource_id = related_resource_id

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this GovernanceRule.
        Date and time the governance rule was created. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this GovernanceRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this GovernanceRule.
        Date and time the governance rule was created. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this GovernanceRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this GovernanceRule.
        Date and time the governance rule was updated. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_updated of this GovernanceRule.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this GovernanceRule.
        Date and time the governance rule was updated. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_updated: The time_updated of this GovernanceRule.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this GovernanceRule.
        The current state of the governance rule.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this GovernanceRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this GovernanceRule.
        The current state of the governance rule.


        :param lifecycle_state: The lifecycle_state of this GovernanceRule.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def freeform_tags(self):
        """
        **[Required]** Gets the freeform_tags of this GovernanceRule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this GovernanceRule.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this GovernanceRule.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this GovernanceRule.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        **[Required]** Gets the defined_tags of this GovernanceRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this GovernanceRule.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this GovernanceRule.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this GovernanceRule.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this GovernanceRule.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this GovernanceRule.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this GovernanceRule.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this GovernanceRule.
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
