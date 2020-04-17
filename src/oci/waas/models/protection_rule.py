# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionRule(object):
    """
    The protection rule settings. Protection rules can allow, block, or trigger an alert if a request meets the parameters of an applied rule.
    """

    #: A constant which can be used with the action property of a ProtectionRule.
    #: This constant has a value of "OFF"
    ACTION_OFF = "OFF"

    #: A constant which can be used with the action property of a ProtectionRule.
    #: This constant has a value of "DETECT"
    ACTION_DETECT = "DETECT"

    #: A constant which can be used with the action property of a ProtectionRule.
    #: This constant has a value of "BLOCK"
    ACTION_BLOCK = "BLOCK"

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionRule object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this ProtectionRule.
        :type key: str

        :param mod_security_rule_ids:
            The value to assign to the mod_security_rule_ids property of this ProtectionRule.
        :type mod_security_rule_ids: list[str]

        :param name:
            The value to assign to the name property of this ProtectionRule.
        :type name: str

        :param description:
            The value to assign to the description property of this ProtectionRule.
        :type description: str

        :param action:
            The value to assign to the action property of this ProtectionRule.
            Allowed values for this property are: "OFF", "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type action: str

        :param labels:
            The value to assign to the labels property of this ProtectionRule.
        :type labels: list[str]

        :param exclusions:
            The value to assign to the exclusions property of this ProtectionRule.
        :type exclusions: list[ProtectionRuleExclusion]

        """
        self.swagger_types = {
            'key': 'str',
            'mod_security_rule_ids': 'list[str]',
            'name': 'str',
            'description': 'str',
            'action': 'str',
            'labels': 'list[str]',
            'exclusions': 'list[ProtectionRuleExclusion]'
        }

        self.attribute_map = {
            'key': 'key',
            'mod_security_rule_ids': 'modSecurityRuleIds',
            'name': 'name',
            'description': 'description',
            'action': 'action',
            'labels': 'labels',
            'exclusions': 'exclusions'
        }

        self._key = None
        self._mod_security_rule_ids = None
        self._name = None
        self._description = None
        self._action = None
        self._labels = None
        self._exclusions = None

    @property
    def key(self):
        """
        Gets the key of this ProtectionRule.
        The unique key of the protection rule.


        :return: The key of this ProtectionRule.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this ProtectionRule.
        The unique key of the protection rule.


        :param key: The key of this ProtectionRule.
        :type: str
        """
        self._key = key

    @property
    def mod_security_rule_ids(self):
        """
        Gets the mod_security_rule_ids of this ProtectionRule.
        The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see `Mod Security's documentation`__.

        __ https://www.modsecurity.org/CRS/Documentation/index.html


        :return: The mod_security_rule_ids of this ProtectionRule.
        :rtype: list[str]
        """
        return self._mod_security_rule_ids

    @mod_security_rule_ids.setter
    def mod_security_rule_ids(self, mod_security_rule_ids):
        """
        Sets the mod_security_rule_ids of this ProtectionRule.
        The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF rules, see `Mod Security's documentation`__.

        __ https://www.modsecurity.org/CRS/Documentation/index.html


        :param mod_security_rule_ids: The mod_security_rule_ids of this ProtectionRule.
        :type: list[str]
        """
        self._mod_security_rule_ids = mod_security_rule_ids

    @property
    def name(self):
        """
        Gets the name of this ProtectionRule.
        The name of the protection rule.


        :return: The name of this ProtectionRule.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ProtectionRule.
        The name of the protection rule.


        :param name: The name of this ProtectionRule.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this ProtectionRule.
        The description of the protection rule.


        :return: The description of this ProtectionRule.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ProtectionRule.
        The description of the protection rule.


        :param description: The description of this ProtectionRule.
        :type: str
        """
        self._description = description

    @property
    def action(self):
        """
        Gets the action of this ProtectionRule.
        The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.

        Allowed values for this property are: "OFF", "DETECT", "BLOCK", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The action of this ProtectionRule.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """
        Sets the action of this ProtectionRule.
        The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.


        :param action: The action of this ProtectionRule.
        :type: str
        """
        allowed_values = ["OFF", "DETECT", "BLOCK"]
        if not value_allowed_none_or_none_sentinel(action, allowed_values):
            action = 'UNKNOWN_ENUM_VALUE'
        self._action = action

    @property
    def labels(self):
        """
        Gets the labels of this ProtectionRule.
        The list of labels for the protection rule.

        **Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true.


        :return: The labels of this ProtectionRule.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this ProtectionRule.
        The list of labels for the protection rule.

        **Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true.


        :param labels: The labels of this ProtectionRule.
        :type: list[str]
        """
        self._labels = labels

    @property
    def exclusions(self):
        """
        Gets the exclusions of this ProtectionRule.

        :return: The exclusions of this ProtectionRule.
        :rtype: list[ProtectionRuleExclusion]
        """
        return self._exclusions

    @exclusions.setter
    def exclusions(self, exclusions):
        """
        Sets the exclusions of this ProtectionRule.

        :param exclusions: The exclusions of this ProtectionRule.
        :type: list[ProtectionRuleExclusion]
        """
        self._exclusions = exclusions

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
