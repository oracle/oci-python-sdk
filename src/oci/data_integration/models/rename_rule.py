# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .projection_rule import ProjectionRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RenameRule(ProjectionRule):
    """
    Lets you rename an attribute.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RenameRule object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.RenameRule.model_type` attribute
        of this class is ``RENAME_RULE`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this RenameRule.
            Allowed values for this property are: "NAME_PATTERN_RULE", "TYPE_LIST_RULE", "NAME_LIST_RULE", "TYPED_NAME_PATTERN_RULE", "RENAME_RULE"
        :type model_type: str

        :param key:
            The value to assign to the key property of this RenameRule.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this RenameRule.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this RenameRule.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param is_java_regex_syntax:
            The value to assign to the is_java_regex_syntax property of this RenameRule.
        :type is_java_regex_syntax: bool

        :param config_values:
            The value to assign to the config_values property of this RenameRule.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this RenameRule.
        :type object_status: int

        :param description:
            The value to assign to the description property of this RenameRule.
        :type description: str

        :param is_skip_remaining_rules_on_match:
            The value to assign to the is_skip_remaining_rules_on_match property of this RenameRule.
        :type is_skip_remaining_rules_on_match: bool

        :param from_name:
            The value to assign to the from_name property of this RenameRule.
        :type from_name: str

        :param to_name:
            The value to assign to the to_name property of this RenameRule.
        :type to_name: str

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
            'is_skip_remaining_rules_on_match': 'bool',
            'from_name': 'str',
            'to_name': 'str'
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
            'is_skip_remaining_rules_on_match': 'isSkipRemainingRulesOnMatch',
            'from_name': 'fromName',
            'to_name': 'toName'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._is_java_regex_syntax = None
        self._config_values = None
        self._object_status = None
        self._description = None
        self._is_skip_remaining_rules_on_match = None
        self._from_name = None
        self._to_name = None
        self._model_type = 'RENAME_RULE'

    @property
    def is_skip_remaining_rules_on_match(self):
        """
        Gets the is_skip_remaining_rules_on_match of this RenameRule.
        Specifies whether to skip remaining rules when a match is found.


        :return: The is_skip_remaining_rules_on_match of this RenameRule.
        :rtype: bool
        """
        return self._is_skip_remaining_rules_on_match

    @is_skip_remaining_rules_on_match.setter
    def is_skip_remaining_rules_on_match(self, is_skip_remaining_rules_on_match):
        """
        Sets the is_skip_remaining_rules_on_match of this RenameRule.
        Specifies whether to skip remaining rules when a match is found.


        :param is_skip_remaining_rules_on_match: The is_skip_remaining_rules_on_match of this RenameRule.
        :type: bool
        """
        self._is_skip_remaining_rules_on_match = is_skip_remaining_rules_on_match

    @property
    def from_name(self):
        """
        Gets the from_name of this RenameRule.
        The attribute name that needs to be renamed.


        :return: The from_name of this RenameRule.
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """
        Sets the from_name of this RenameRule.
        The attribute name that needs to be renamed.


        :param from_name: The from_name of this RenameRule.
        :type: str
        """
        self._from_name = from_name

    @property
    def to_name(self):
        """
        Gets the to_name of this RenameRule.
        The new attribute name.


        :return: The to_name of this RenameRule.
        :rtype: str
        """
        return self._to_name

    @to_name.setter
    def to_name(self, to_name):
        """
        Sets the to_name of this RenameRule.
        The new attribute name.


        :param to_name: The to_name of this RenameRule.
        :type: str
        """
        self._to_name = to_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
