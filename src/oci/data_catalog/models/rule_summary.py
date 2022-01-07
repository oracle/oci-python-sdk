# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RuleSummary(object):
    """
    A list of rule resources. One or more rules can be defined for a data entity.
    Each rule can be defined on one or more attributes of the data entity.
    """

    #: A constant which can be used with the rule_type property of a RuleSummary.
    #: This constant has a value of "PRIMARYKEY"
    RULE_TYPE_PRIMARYKEY = "PRIMARYKEY"

    #: A constant which can be used with the rule_type property of a RuleSummary.
    #: This constant has a value of "FOREIGNKEY"
    RULE_TYPE_FOREIGNKEY = "FOREIGNKEY"

    #: A constant which can be used with the rule_type property of a RuleSummary.
    #: This constant has a value of "UNIQUEKEY"
    RULE_TYPE_UNIQUEKEY = "UNIQUEKEY"

    #: A constant which can be used with the origin_type property of a RuleSummary.
    #: This constant has a value of "SOURCE"
    ORIGIN_TYPE_SOURCE = "SOURCE"

    #: A constant which can be used with the origin_type property of a RuleSummary.
    #: This constant has a value of "USER"
    ORIGIN_TYPE_USER = "USER"

    #: A constant which can be used with the origin_type property of a RuleSummary.
    #: This constant has a value of "PROFILING"
    ORIGIN_TYPE_PROFILING = "PROFILING"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a RuleSummary.
    #: This constant has a value of "MOVING"
    LIFECYCLE_STATE_MOVING = "MOVING"

    def __init__(self, **kwargs):
        """
        Initializes a new RuleSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this RuleSummary.
        :type key: str

        :param display_name:
            The value to assign to the display_name property of this RuleSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this RuleSummary.
        :type description: str

        :param rule_type:
            The value to assign to the rule_type property of this RuleSummary.
            Allowed values for this property are: "PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_type: str

        :param external_key:
            The value to assign to the external_key property of this RuleSummary.
        :type external_key: str

        :param attributes:
            The value to assign to the attributes property of this RuleSummary.
        :type attributes: list[oci.data_catalog.models.RuleAttribute]

        :param referenced_folder_key:
            The value to assign to the referenced_folder_key property of this RuleSummary.
        :type referenced_folder_key: str

        :param referenced_folder_name:
            The value to assign to the referenced_folder_name property of this RuleSummary.
        :type referenced_folder_name: str

        :param referenced_entity_key:
            The value to assign to the referenced_entity_key property of this RuleSummary.
        :type referenced_entity_key: str

        :param referenced_entity_name:
            The value to assign to the referenced_entity_name property of this RuleSummary.
        :type referenced_entity_name: str

        :param referenced_rule_key:
            The value to assign to the referenced_rule_key property of this RuleSummary.
        :type referenced_rule_key: str

        :param referenced_rule_name:
            The value to assign to the referenced_rule_name property of this RuleSummary.
        :type referenced_rule_name: str

        :param referenced_attributes:
            The value to assign to the referenced_attributes property of this RuleSummary.
        :type referenced_attributes: list[oci.data_catalog.models.RuleAttribute]

        :param origin_type:
            The value to assign to the origin_type property of this RuleSummary.
            Allowed values for this property are: "SOURCE", "USER", "PROFILING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type origin_type: str

        :param uri:
            The value to assign to the uri property of this RuleSummary.
        :type uri: str

        :param time_created:
            The value to assign to the time_created property of this RuleSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this RuleSummary.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'key': 'str',
            'display_name': 'str',
            'description': 'str',
            'rule_type': 'str',
            'external_key': 'str',
            'attributes': 'list[RuleAttribute]',
            'referenced_folder_key': 'str',
            'referenced_folder_name': 'str',
            'referenced_entity_key': 'str',
            'referenced_entity_name': 'str',
            'referenced_rule_key': 'str',
            'referenced_rule_name': 'str',
            'referenced_attributes': 'list[RuleAttribute]',
            'origin_type': 'str',
            'uri': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'display_name': 'displayName',
            'description': 'description',
            'rule_type': 'ruleType',
            'external_key': 'externalKey',
            'attributes': 'attributes',
            'referenced_folder_key': 'referencedFolderKey',
            'referenced_folder_name': 'referencedFolderName',
            'referenced_entity_key': 'referencedEntityKey',
            'referenced_entity_name': 'referencedEntityName',
            'referenced_rule_key': 'referencedRuleKey',
            'referenced_rule_name': 'referencedRuleName',
            'referenced_attributes': 'referencedAttributes',
            'origin_type': 'originType',
            'uri': 'uri',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState'
        }

        self._key = None
        self._display_name = None
        self._description = None
        self._rule_type = None
        self._external_key = None
        self._attributes = None
        self._referenced_folder_key = None
        self._referenced_folder_name = None
        self._referenced_entity_key = None
        self._referenced_entity_name = None
        self._referenced_rule_key = None
        self._referenced_rule_name = None
        self._referenced_attributes = None
        self._origin_type = None
        self._uri = None
        self._time_created = None
        self._lifecycle_state = None

    @property
    def key(self):
        """
        **[Required]** Gets the key of this RuleSummary.
        Immutable unique key of a rule.


        :return: The key of this RuleSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this RuleSummary.
        Immutable unique key of a rule.


        :param key: The key of this RuleSummary.
        :type: str
        """
        self._key = key

    @property
    def display_name(self):
        """
        Gets the display_name of this RuleSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :return: The display_name of this RuleSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this RuleSummary.
        A user-friendly display name. Does not have to be unique, and it's changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this RuleSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this RuleSummary.
        Detailed description of a rule.


        :return: The description of this RuleSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this RuleSummary.
        Detailed description of a rule.


        :param description: The description of this RuleSummary.
        :type: str
        """
        self._description = description

    @property
    def rule_type(self):
        """
        Gets the rule_type of this RuleSummary.
        Type of a rule.

        Allowed values for this property are: "PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_type of this RuleSummary.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this RuleSummary.
        Type of a rule.


        :param rule_type: The rule_type of this RuleSummary.
        :type: str
        """
        allowed_values = ["PRIMARYKEY", "FOREIGNKEY", "UNIQUEKEY"]
        if not value_allowed_none_or_none_sentinel(rule_type, allowed_values):
            rule_type = 'UNKNOWN_ENUM_VALUE'
        self._rule_type = rule_type

    @property
    def external_key(self):
        """
        Gets the external_key of this RuleSummary.
        External URI that can be used to reference the object. Format will differ based on the type of object.


        :return: The external_key of this RuleSummary.
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """
        Sets the external_key of this RuleSummary.
        External URI that can be used to reference the object. Format will differ based on the type of object.


        :param external_key: The external_key of this RuleSummary.
        :type: str
        """
        self._external_key = external_key

    @property
    def attributes(self):
        """
        Gets the attributes of this RuleSummary.
        Attributes associated with a rule.
        A UNIQUEKEY rule would contain (at least) one attribute, for the local table column(s) on which uniqueness is defined.


        :return: The attributes of this RuleSummary.
        :rtype: list[oci.data_catalog.models.RuleAttribute]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this RuleSummary.
        Attributes associated with a rule.
        A UNIQUEKEY rule would contain (at least) one attribute, for the local table column(s) on which uniqueness is defined.


        :param attributes: The attributes of this RuleSummary.
        :type: list[oci.data_catalog.models.RuleAttribute]
        """
        self._attributes = attributes

    @property
    def referenced_folder_key(self):
        """
        Gets the referenced_folder_key of this RuleSummary.
        Folder key that represents the referenced folder, applicable only when rule type FOREIGNKEY.


        :return: The referenced_folder_key of this RuleSummary.
        :rtype: str
        """
        return self._referenced_folder_key

    @referenced_folder_key.setter
    def referenced_folder_key(self, referenced_folder_key):
        """
        Sets the referenced_folder_key of this RuleSummary.
        Folder key that represents the referenced folder, applicable only when rule type FOREIGNKEY.


        :param referenced_folder_key: The referenced_folder_key of this RuleSummary.
        :type: str
        """
        self._referenced_folder_key = referenced_folder_key

    @property
    def referenced_folder_name(self):
        """
        Gets the referenced_folder_name of this RuleSummary.
        Folder name that represents the referenced folder, applicable only when rule type FOREIGNKEY.


        :return: The referenced_folder_name of this RuleSummary.
        :rtype: str
        """
        return self._referenced_folder_name

    @referenced_folder_name.setter
    def referenced_folder_name(self, referenced_folder_name):
        """
        Sets the referenced_folder_name of this RuleSummary.
        Folder name that represents the referenced folder, applicable only when rule type FOREIGNKEY.


        :param referenced_folder_name: The referenced_folder_name of this RuleSummary.
        :type: str
        """
        self._referenced_folder_name = referenced_folder_name

    @property
    def referenced_entity_key(self):
        """
        Gets the referenced_entity_key of this RuleSummary.
        Entity key that represents the referenced entity, applicable only when rule type is FOREIGNKEY.


        :return: The referenced_entity_key of this RuleSummary.
        :rtype: str
        """
        return self._referenced_entity_key

    @referenced_entity_key.setter
    def referenced_entity_key(self, referenced_entity_key):
        """
        Sets the referenced_entity_key of this RuleSummary.
        Entity key that represents the referenced entity, applicable only when rule type is FOREIGNKEY.


        :param referenced_entity_key: The referenced_entity_key of this RuleSummary.
        :type: str
        """
        self._referenced_entity_key = referenced_entity_key

    @property
    def referenced_entity_name(self):
        """
        Gets the referenced_entity_name of this RuleSummary.
        Entity name that represents the referenced entity, applicable only when rule type is FOREIGNKEY.


        :return: The referenced_entity_name of this RuleSummary.
        :rtype: str
        """
        return self._referenced_entity_name

    @referenced_entity_name.setter
    def referenced_entity_name(self, referenced_entity_name):
        """
        Sets the referenced_entity_name of this RuleSummary.
        Entity name that represents the referenced entity, applicable only when rule type is FOREIGNKEY.


        :param referenced_entity_name: The referenced_entity_name of this RuleSummary.
        :type: str
        """
        self._referenced_entity_name = referenced_entity_name

    @property
    def referenced_rule_key(self):
        """
        Gets the referenced_rule_key of this RuleSummary.
        Rule key that represents the referenced rule, applicable only when rule type is FOREIGNKEY.


        :return: The referenced_rule_key of this RuleSummary.
        :rtype: str
        """
        return self._referenced_rule_key

    @referenced_rule_key.setter
    def referenced_rule_key(self, referenced_rule_key):
        """
        Sets the referenced_rule_key of this RuleSummary.
        Rule key that represents the referenced rule, applicable only when rule type is FOREIGNKEY.


        :param referenced_rule_key: The referenced_rule_key of this RuleSummary.
        :type: str
        """
        self._referenced_rule_key = referenced_rule_key

    @property
    def referenced_rule_name(self):
        """
        Gets the referenced_rule_name of this RuleSummary.
        Rule name that represents the referenced rule, applicable only when rule type is FOREIGNKEY.


        :return: The referenced_rule_name of this RuleSummary.
        :rtype: str
        """
        return self._referenced_rule_name

    @referenced_rule_name.setter
    def referenced_rule_name(self, referenced_rule_name):
        """
        Sets the referenced_rule_name of this RuleSummary.
        Rule name that represents the referenced rule, applicable only when rule type is FOREIGNKEY.


        :param referenced_rule_name: The referenced_rule_name of this RuleSummary.
        :type: str
        """
        self._referenced_rule_name = referenced_rule_name

    @property
    def referenced_attributes(self):
        """
        Gets the referenced_attributes of this RuleSummary.
        Attributes associated with referenced rule, applicable only when rule type is FOREIGNKEY.
        A FOREIGNKEY rule would contain (at least) one attribute, for the local table column(s), and (at least) one referencedAttribute for referenced table column(s).


        :return: The referenced_attributes of this RuleSummary.
        :rtype: list[oci.data_catalog.models.RuleAttribute]
        """
        return self._referenced_attributes

    @referenced_attributes.setter
    def referenced_attributes(self, referenced_attributes):
        """
        Sets the referenced_attributes of this RuleSummary.
        Attributes associated with referenced rule, applicable only when rule type is FOREIGNKEY.
        A FOREIGNKEY rule would contain (at least) one attribute, for the local table column(s), and (at least) one referencedAttribute for referenced table column(s).


        :param referenced_attributes: The referenced_attributes of this RuleSummary.
        :type: list[oci.data_catalog.models.RuleAttribute]
        """
        self._referenced_attributes = referenced_attributes

    @property
    def origin_type(self):
        """
        Gets the origin_type of this RuleSummary.
        Origin type of the rule.

        Allowed values for this property are: "SOURCE", "USER", "PROFILING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The origin_type of this RuleSummary.
        :rtype: str
        """
        return self._origin_type

    @origin_type.setter
    def origin_type(self, origin_type):
        """
        Sets the origin_type of this RuleSummary.
        Origin type of the rule.


        :param origin_type: The origin_type of this RuleSummary.
        :type: str
        """
        allowed_values = ["SOURCE", "USER", "PROFILING"]
        if not value_allowed_none_or_none_sentinel(origin_type, allowed_values):
            origin_type = 'UNKNOWN_ENUM_VALUE'
        self._origin_type = origin_type

    @property
    def uri(self):
        """
        Gets the uri of this RuleSummary.
        URI to the rule instance in the API.


        :return: The uri of this RuleSummary.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this RuleSummary.
        URI to the rule instance in the API.


        :param uri: The uri of this RuleSummary.
        :type: str
        """
        self._uri = uri

    @property
    def time_created(self):
        """
        Gets the time_created of this RuleSummary.
        The date and time the rule was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this RuleSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this RuleSummary.
        The date and time the rule was created, in the format defined by `RFC3339`__.
        Example: `2019-03-25T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this RuleSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this RuleSummary.
        State of the rule.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this RuleSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this RuleSummary.
        State of the rule.


        :param lifecycle_state: The lifecycle_state of this RuleSummary.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", "MOVING"]
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
