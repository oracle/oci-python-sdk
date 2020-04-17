# coding: utf-8
# Copyright (c) 2016, 2020, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Recommendation(object):
    """
    A recommended protection rule for a web application. This recommendation can be accepted to apply it to the Web Application Firewall configuration for this policy.

    Use the `POST /waasPolicies/{waasPolicyId}/actions/acceptWafConfigRecommendations` method to accept recommended protection rules.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Recommendation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this Recommendation.
        :type key: str

        :param mod_security_rule_ids:
            The value to assign to the mod_security_rule_ids property of this Recommendation.
        :type mod_security_rule_ids: list[str]

        :param name:
            The value to assign to the name property of this Recommendation.
        :type name: str

        :param description:
            The value to assign to the description property of this Recommendation.
        :type description: str

        :param labels:
            The value to assign to the labels property of this Recommendation.
        :type labels: list[str]

        :param recommended_action:
            The value to assign to the recommended_action property of this Recommendation.
        :type recommended_action: str

        """
        self.swagger_types = {
            'key': 'str',
            'mod_security_rule_ids': 'list[str]',
            'name': 'str',
            'description': 'str',
            'labels': 'list[str]',
            'recommended_action': 'str'
        }

        self.attribute_map = {
            'key': 'key',
            'mod_security_rule_ids': 'modSecurityRuleIds',
            'name': 'name',
            'description': 'description',
            'labels': 'labels',
            'recommended_action': 'recommendedAction'
        }

        self._key = None
        self._mod_security_rule_ids = None
        self._name = None
        self._description = None
        self._labels = None
        self._recommended_action = None

    @property
    def key(self):
        """
        Gets the key of this Recommendation.
        The unique key for the recommended protection rule.


        :return: The key of this Recommendation.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this Recommendation.
        The unique key for the recommended protection rule.


        :param key: The key of this Recommendation.
        :type: str
        """
        self._key = key

    @property
    def mod_security_rule_ids(self):
        """
        Gets the mod_security_rule_ids of this Recommendation.
        The list of the ModSecurity rule IDs associated with the protection rule.
        For more information about ModSecurity's open source WAF rules, see `Mod Security's documentation`__.

        __ https://www.modsecurity.org/CRS/Documentation/index.html


        :return: The mod_security_rule_ids of this Recommendation.
        :rtype: list[str]
        """
        return self._mod_security_rule_ids

    @mod_security_rule_ids.setter
    def mod_security_rule_ids(self, mod_security_rule_ids):
        """
        Sets the mod_security_rule_ids of this Recommendation.
        The list of the ModSecurity rule IDs associated with the protection rule.
        For more information about ModSecurity's open source WAF rules, see `Mod Security's documentation`__.

        __ https://www.modsecurity.org/CRS/Documentation/index.html


        :param mod_security_rule_ids: The mod_security_rule_ids of this Recommendation.
        :type: list[str]
        """
        self._mod_security_rule_ids = mod_security_rule_ids

    @property
    def name(self):
        """
        Gets the name of this Recommendation.
        The name of the recommended protection rule.


        :return: The name of this Recommendation.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this Recommendation.
        The name of the recommended protection rule.


        :param name: The name of this Recommendation.
        :type: str
        """
        self._name = name

    @property
    def description(self):
        """
        Gets the description of this Recommendation.
        The description of the recommended protection rule.


        :return: The description of this Recommendation.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this Recommendation.
        The description of the recommended protection rule.


        :param description: The description of this Recommendation.
        :type: str
        """
        self._description = description

    @property
    def labels(self):
        """
        Gets the labels of this Recommendation.
        The list of labels for the recommended protection rule.


        :return: The labels of this Recommendation.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """
        Sets the labels of this Recommendation.
        The list of labels for the recommended protection rule.


        :param labels: The labels of this Recommendation.
        :type: list[str]
        """
        self._labels = labels

    @property
    def recommended_action(self):
        """
        Gets the recommended_action of this Recommendation.
        The recommended action to apply to the protection rule.


        :return: The recommended_action of this Recommendation.
        :rtype: str
        """
        return self._recommended_action

    @recommended_action.setter
    def recommended_action(self, recommended_action):
        """
        Sets the recommended_action of this Recommendation.
        The recommended action to apply to the protection rule.


        :param recommended_action: The recommended_action of this Recommendation.
        :type: str
        """
        self._recommended_action = recommended_action

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
