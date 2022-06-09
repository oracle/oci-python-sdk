# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class EnforcedGovernanceRule(object):
    """
    Represents the governance rule shown to the child which is a subset of governance rule resource in parent tenancy.
    """

    #: A constant which can be used with the type property of a EnforcedGovernanceRule.
    #: This constant has a value of "QUOTA"
    TYPE_QUOTA = "QUOTA"

    #: A constant which can be used with the type property of a EnforcedGovernanceRule.
    #: This constant has a value of "TAG"
    TYPE_TAG = "TAG"

    #: A constant which can be used with the type property of a EnforcedGovernanceRule.
    #: This constant has a value of "ALLOWED_REGIONS"
    TYPE_ALLOWED_REGIONS = "ALLOWED_REGIONS"

    #: A constant which can be used with the lifecycle_state property of a EnforcedGovernanceRule.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a EnforcedGovernanceRule.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new EnforcedGovernanceRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this EnforcedGovernanceRule.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this EnforcedGovernanceRule.
        :type compartment_id: str

        :param governance_rule_display_name:
            The value to assign to the governance_rule_display_name property of this EnforcedGovernanceRule.
        :type governance_rule_display_name: str

        :param type:
            The value to assign to the type property of this EnforcedGovernanceRule.
            Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param template:
            The value to assign to the template property of this EnforcedGovernanceRule.
        :type template: oci.governance_rules_control_plane.models.Template

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this EnforcedGovernanceRule.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this EnforcedGovernanceRule.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this EnforcedGovernanceRule.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'governance_rule_display_name': 'str',
            'type': 'str',
            'template': 'Template',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'governance_rule_display_name': 'governanceRuleDisplayName',
            'type': 'type',
            'template': 'template',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._compartment_id = None
        self._governance_rule_display_name = None
        self._type = None
        self._template = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this EnforcedGovernanceRule.
        The Oracle ID (`OCID`__) of the enforced governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this EnforcedGovernanceRule.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this EnforcedGovernanceRule.
        The Oracle ID (`OCID`__) of the enforced governance rule.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this EnforcedGovernanceRule.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this EnforcedGovernanceRule.
        The Oracle ID (`OCID`__) of the child's root compartment to which the governance rule is attached.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this EnforcedGovernanceRule.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this EnforcedGovernanceRule.
        The Oracle ID (`OCID`__) of the child's root compartment to which the governance rule is attached.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this EnforcedGovernanceRule.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def governance_rule_display_name(self):
        """
        **[Required]** Gets the governance_rule_display_name of this EnforcedGovernanceRule.
        Display name of the governance rule.


        :return: The governance_rule_display_name of this EnforcedGovernanceRule.
        :rtype: str
        """
        return self._governance_rule_display_name

    @governance_rule_display_name.setter
    def governance_rule_display_name(self, governance_rule_display_name):
        """
        Sets the governance_rule_display_name of this EnforcedGovernanceRule.
        Display name of the governance rule.


        :param governance_rule_display_name: The governance_rule_display_name of this EnforcedGovernanceRule.
        :type: str
        """
        self._governance_rule_display_name = governance_rule_display_name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this EnforcedGovernanceRule.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`

        Allowed values for this property are: "QUOTA", "TAG", "ALLOWED_REGIONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this EnforcedGovernanceRule.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this EnforcedGovernanceRule.
        Type of the governance rule, can be one of QUOTA, TAG, ALLOWED_REGIONS.

        Example: `QUOTA`


        :param type: The type of this EnforcedGovernanceRule.
        :type: str
        """
        allowed_values = ["QUOTA", "TAG", "ALLOWED_REGIONS"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def template(self):
        """
        **[Required]** Gets the template of this EnforcedGovernanceRule.

        :return: The template of this EnforcedGovernanceRule.
        :rtype: oci.governance_rules_control_plane.models.Template
        """
        return self._template

    @template.setter
    def template(self, template):
        """
        Sets the template of this EnforcedGovernanceRule.

        :param template: The template of this EnforcedGovernanceRule.
        :type: oci.governance_rules_control_plane.models.Template
        """
        self._template = template

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this EnforcedGovernanceRule.
        The current state of the governance rule.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this EnforcedGovernanceRule.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this EnforcedGovernanceRule.
        The current state of the governance rule.


        :param lifecycle_state: The lifecycle_state of this EnforcedGovernanceRule.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this EnforcedGovernanceRule.
        Date and time the governance rule was created. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_created of this EnforcedGovernanceRule.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this EnforcedGovernanceRule.
        Date and time the governance rule was created. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_created: The time_created of this EnforcedGovernanceRule.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this EnforcedGovernanceRule.
        Date and time the governance rule was updated. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :return: The time_updated of this EnforcedGovernanceRule.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this EnforcedGovernanceRule.
        Date and time the governance rule was updated. An RFC3339 formatted datetime string.

        Example: `2016-08-25T21:10:29.600Z`


        :param time_updated: The time_updated of this EnforcedGovernanceRule.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
