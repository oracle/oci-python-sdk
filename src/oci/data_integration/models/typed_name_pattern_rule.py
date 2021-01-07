# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .projection_rule import ProjectionRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TypedNamePatternRule(ProjectionRule):
    """
    The typed name rule for field projection.
    """

    #: A constant which can be used with the matching_strategy property of a TypedNamePatternRule.
    #: This constant has a value of "NAME_OR_TAGS"
    MATCHING_STRATEGY_NAME_OR_TAGS = "NAME_OR_TAGS"

    #: A constant which can be used with the matching_strategy property of a TypedNamePatternRule.
    #: This constant has a value of "TAGS_ONLY"
    MATCHING_STRATEGY_TAGS_ONLY = "TAGS_ONLY"

    #: A constant which can be used with the matching_strategy property of a TypedNamePatternRule.
    #: This constant has a value of "NAME_ONLY"
    MATCHING_STRATEGY_NAME_ONLY = "NAME_ONLY"

    #: A constant which can be used with the rule_type property of a TypedNamePatternRule.
    #: This constant has a value of "INCLUDE"
    RULE_TYPE_INCLUDE = "INCLUDE"

    #: A constant which can be used with the rule_type property of a TypedNamePatternRule.
    #: This constant has a value of "EXCLUDE"
    RULE_TYPE_EXCLUDE = "EXCLUDE"

    def __init__(self, **kwargs):
        """
        Initializes a new TypedNamePatternRule object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.TypedNamePatternRule.model_type` attribute
        of this class is ``TYPED_NAME_PATTERN_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this TypedNamePatternRule.
            Allowed values for this property are: "NAME_PATTERN_RULE", "TYPE_LIST_RULE", "NAME_LIST_RULE", "TYPED_NAME_PATTERN_RULE", "RENAME_RULE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this TypedNamePatternRule.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this TypedNamePatternRule.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this TypedNamePatternRule.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param is_java_regex_syntax:
            The value to assign to the is_java_regex_syntax property of this TypedNamePatternRule.
        :type is_java_regex_syntax: bool

        :param config_values:
            The value to assign to the config_values property of this TypedNamePatternRule.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this TypedNamePatternRule.
        :type object_status: int

        :param description:
            The value to assign to the description property of this TypedNamePatternRule.
        :type description: str

        :param types:
            The value to assign to the types property of this TypedNamePatternRule.
        :type types: list[object]

        :param is_skip_remaining_rules_on_match:
            The value to assign to the is_skip_remaining_rules_on_match property of this TypedNamePatternRule.
        :type is_skip_remaining_rules_on_match: bool

        :param scope:
            The value to assign to the scope property of this TypedNamePatternRule.
        :type scope: object

        :param is_cascade:
            The value to assign to the is_cascade property of this TypedNamePatternRule.
        :type is_cascade: bool

        :param matching_strategy:
            The value to assign to the matching_strategy property of this TypedNamePatternRule.
            Allowed values for this property are: "NAME_OR_TAGS", "TAGS_ONLY", "NAME_ONLY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type matching_strategy: str

        :param is_case_sensitive:
            The value to assign to the is_case_sensitive property of this TypedNamePatternRule.
        :type is_case_sensitive: bool

        :param rule_type:
            The value to assign to the rule_type property of this TypedNamePatternRule.
            Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type rule_type: str

        :param pattern:
            The value to assign to the pattern property of this TypedNamePatternRule.
        :type pattern: str

        :param names:
            The value to assign to the names property of this TypedNamePatternRule.
        :type names: list[str]

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'is_java_regex_syntax': 'bool',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'description': 'str',
            'types': 'list[object]',
            'is_skip_remaining_rules_on_match': 'bool',
            'scope': 'object',
            'is_cascade': 'bool',
            'matching_strategy': 'str',
            'is_case_sensitive': 'bool',
            'rule_type': 'str',
            'pattern': 'str',
            'names': 'list[str]'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'is_java_regex_syntax': 'isJavaRegexSyntax',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'description': 'description',
            'types': 'types',
            'is_skip_remaining_rules_on_match': 'isSkipRemainingRulesOnMatch',
            'scope': 'scope',
            'is_cascade': 'isCascade',
            'matching_strategy': 'matchingStrategy',
            'is_case_sensitive': 'isCaseSensitive',
            'rule_type': 'ruleType',
            'pattern': 'pattern',
            'names': 'names'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._is_java_regex_syntax = None
        self._config_values = None
        self._object_status = None
        self._description = None
        self._types = None
        self._is_skip_remaining_rules_on_match = None
        self._scope = None
        self._is_cascade = None
        self._matching_strategy = None
        self._is_case_sensitive = None
        self._rule_type = None
        self._pattern = None
        self._names = None
        self._model_type = 'TYPED_NAME_PATTERN_RULE'

    @property
    def types(self):
        """
        Gets the types of this TypedNamePatternRule.
        An array of types.


        :return: The types of this TypedNamePatternRule.
        :rtype: list[object]
        """
        return self._types

    @types.setter
    def types(self, types):
        """
        Sets the types of this TypedNamePatternRule.
        An array of types.


        :param types: The types of this TypedNamePatternRule.
        :type: list[object]
        """
        self._types = types

    @property
    def is_skip_remaining_rules_on_match(self):
        """
        Gets the is_skip_remaining_rules_on_match of this TypedNamePatternRule.
        Specifies whether to skip remaining rules when a match is found.


        :return: The is_skip_remaining_rules_on_match of this TypedNamePatternRule.
        :rtype: bool
        """
        return self._is_skip_remaining_rules_on_match

    @is_skip_remaining_rules_on_match.setter
    def is_skip_remaining_rules_on_match(self, is_skip_remaining_rules_on_match):
        """
        Sets the is_skip_remaining_rules_on_match of this TypedNamePatternRule.
        Specifies whether to skip remaining rules when a match is found.


        :param is_skip_remaining_rules_on_match: The is_skip_remaining_rules_on_match of this TypedNamePatternRule.
        :type: bool
        """
        self._is_skip_remaining_rules_on_match = is_skip_remaining_rules_on_match

    @property
    def scope(self):
        """
        Gets the scope of this TypedNamePatternRule.
        Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.


        :return: The scope of this TypedNamePatternRule.
        :rtype: object
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this TypedNamePatternRule.
        Reference to a typed object. This can be either a key value to an object within the document, a shall referenced to a `TypedObject`, or a full `TypedObject` definition.


        :param scope: The scope of this TypedNamePatternRule.
        :type: object
        """
        self._scope = scope

    @property
    def is_cascade(self):
        """
        Gets the is_cascade of this TypedNamePatternRule.
        Specifies whether to cascade or not.


        :return: The is_cascade of this TypedNamePatternRule.
        :rtype: bool
        """
        return self._is_cascade

    @is_cascade.setter
    def is_cascade(self, is_cascade):
        """
        Sets the is_cascade of this TypedNamePatternRule.
        Specifies whether to cascade or not.


        :param is_cascade: The is_cascade of this TypedNamePatternRule.
        :type: bool
        """
        self._is_cascade = is_cascade

    @property
    def matching_strategy(self):
        """
        Gets the matching_strategy of this TypedNamePatternRule.
        The pattern matching strategy.

        Allowed values for this property are: "NAME_OR_TAGS", "TAGS_ONLY", "NAME_ONLY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The matching_strategy of this TypedNamePatternRule.
        :rtype: str
        """
        return self._matching_strategy

    @matching_strategy.setter
    def matching_strategy(self, matching_strategy):
        """
        Sets the matching_strategy of this TypedNamePatternRule.
        The pattern matching strategy.


        :param matching_strategy: The matching_strategy of this TypedNamePatternRule.
        :type: str
        """
        allowed_values = ["NAME_OR_TAGS", "TAGS_ONLY", "NAME_ONLY"]
        if not value_allowed_none_or_none_sentinel(matching_strategy, allowed_values):
            matching_strategy = 'UNKNOWN_ENUM_VALUE'
        self._matching_strategy = matching_strategy

    @property
    def is_case_sensitive(self):
        """
        Gets the is_case_sensitive of this TypedNamePatternRule.
        Specifies if the rule is case sensitive.


        :return: The is_case_sensitive of this TypedNamePatternRule.
        :rtype: bool
        """
        return self._is_case_sensitive

    @is_case_sensitive.setter
    def is_case_sensitive(self, is_case_sensitive):
        """
        Sets the is_case_sensitive of this TypedNamePatternRule.
        Specifies if the rule is case sensitive.


        :param is_case_sensitive: The is_case_sensitive of this TypedNamePatternRule.
        :type: bool
        """
        self._is_case_sensitive = is_case_sensitive

    @property
    def rule_type(self):
        """
        Gets the rule_type of this TypedNamePatternRule.
        The rule type.

        Allowed values for this property are: "INCLUDE", "EXCLUDE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The rule_type of this TypedNamePatternRule.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        """
        Sets the rule_type of this TypedNamePatternRule.
        The rule type.


        :param rule_type: The rule_type of this TypedNamePatternRule.
        :type: str
        """
        allowed_values = ["INCLUDE", "EXCLUDE"]
        if not value_allowed_none_or_none_sentinel(rule_type, allowed_values):
            rule_type = 'UNKNOWN_ENUM_VALUE'
        self._rule_type = rule_type

    @property
    def pattern(self):
        """
        Gets the pattern of this TypedNamePatternRule.
        The rule pattern.


        :return: The pattern of this TypedNamePatternRule.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this TypedNamePatternRule.
        The rule pattern.


        :param pattern: The pattern of this TypedNamePatternRule.
        :type: str
        """
        self._pattern = pattern

    @property
    def names(self):
        """
        Gets the names of this TypedNamePatternRule.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The names of this TypedNamePatternRule.
        :rtype: list[str]
        """
        return self._names

    @names.setter
    def names(self, names):
        """
        Sets the names of this TypedNamePatternRule.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param names: The names of this TypedNamePatternRule.
        :type: list[str]
        """
        self._names = names

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
