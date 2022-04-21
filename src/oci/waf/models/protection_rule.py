# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .web_app_firewall_policy_rule import WebAppFirewallPolicyRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ProtectionRule(WebAppFirewallPolicyRule):
    """
    Rule that represents Request/Response Protection.
    Only actions of the following types are allowed to be referenced in this rule:
    * CHECK
    * RETURN_HTTP_RESPONSE
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ProtectionRule object with values from keyword arguments. The default value of the :py:attr:`~oci.waf.models.ProtectionRule.type` attribute
        of this class is ``PROTECTION`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this ProtectionRule.
            Allowed values for this property are: "ACCESS_CONTROL", "PROTECTION", "REQUEST_RATE_LIMITING"
        :type type: str

        :param name:
            The value to assign to the name property of this ProtectionRule.
        :type name: str

        :param condition_language:
            The value to assign to the condition_language property of this ProtectionRule.
            Allowed values for this property are: "JMESPATH"
        :type condition_language: str

        :param condition:
            The value to assign to the condition property of this ProtectionRule.
        :type condition: str

        :param action_name:
            The value to assign to the action_name property of this ProtectionRule.
        :type action_name: str

        :param protection_capabilities:
            The value to assign to the protection_capabilities property of this ProtectionRule.
        :type protection_capabilities: list[oci.waf.models.ProtectionCapability]

        :param protection_capability_settings:
            The value to assign to the protection_capability_settings property of this ProtectionRule.
        :type protection_capability_settings: oci.waf.models.ProtectionCapabilitySettings

        :param is_body_inspection_enabled:
            The value to assign to the is_body_inspection_enabled property of this ProtectionRule.
        :type is_body_inspection_enabled: bool

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'condition_language': 'str',
            'condition': 'str',
            'action_name': 'str',
            'protection_capabilities': 'list[ProtectionCapability]',
            'protection_capability_settings': 'ProtectionCapabilitySettings',
            'is_body_inspection_enabled': 'bool'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'condition_language': 'conditionLanguage',
            'condition': 'condition',
            'action_name': 'actionName',
            'protection_capabilities': 'protectionCapabilities',
            'protection_capability_settings': 'protectionCapabilitySettings',
            'is_body_inspection_enabled': 'isBodyInspectionEnabled'
        }

        self._type = None
        self._name = None
        self._condition_language = None
        self._condition = None
        self._action_name = None
        self._protection_capabilities = None
        self._protection_capability_settings = None
        self._is_body_inspection_enabled = None
        self._type = 'PROTECTION'

    @property
    def protection_capabilities(self):
        """
        **[Required]** Gets the protection_capabilities of this ProtectionRule.
        An ordered list that references OCI-managed protection capabilities.
        Referenced protection capabilities are not necessarily executed in order of appearance. Their execution order
        is decided at runtime for improved performance.
        The array cannot contain entries with the same pair of capability key and version more than once.


        :return: The protection_capabilities of this ProtectionRule.
        :rtype: list[oci.waf.models.ProtectionCapability]
        """
        return self._protection_capabilities

    @protection_capabilities.setter
    def protection_capabilities(self, protection_capabilities):
        """
        Sets the protection_capabilities of this ProtectionRule.
        An ordered list that references OCI-managed protection capabilities.
        Referenced protection capabilities are not necessarily executed in order of appearance. Their execution order
        is decided at runtime for improved performance.
        The array cannot contain entries with the same pair of capability key and version more than once.


        :param protection_capabilities: The protection_capabilities of this ProtectionRule.
        :type: list[oci.waf.models.ProtectionCapability]
        """
        self._protection_capabilities = protection_capabilities

    @property
    def protection_capability_settings(self):
        """
        Gets the protection_capability_settings of this ProtectionRule.

        :return: The protection_capability_settings of this ProtectionRule.
        :rtype: oci.waf.models.ProtectionCapabilitySettings
        """
        return self._protection_capability_settings

    @protection_capability_settings.setter
    def protection_capability_settings(self, protection_capability_settings):
        """
        Sets the protection_capability_settings of this ProtectionRule.

        :param protection_capability_settings: The protection_capability_settings of this ProtectionRule.
        :type: oci.waf.models.ProtectionCapabilitySettings
        """
        self._protection_capability_settings = protection_capability_settings

    @property
    def is_body_inspection_enabled(self):
        """
        Gets the is_body_inspection_enabled of this ProtectionRule.
        Enables/disables body inspection for this protection rule.
        Only Protection Rules in RequestProtection can have this option enabled. Response body inspection will
        be available at a later date.


        :return: The is_body_inspection_enabled of this ProtectionRule.
        :rtype: bool
        """
        return self._is_body_inspection_enabled

    @is_body_inspection_enabled.setter
    def is_body_inspection_enabled(self, is_body_inspection_enabled):
        """
        Sets the is_body_inspection_enabled of this ProtectionRule.
        Enables/disables body inspection for this protection rule.
        Only Protection Rules in RequestProtection can have this option enabled. Response body inspection will
        be available at a later date.


        :param is_body_inspection_enabled: The is_body_inspection_enabled of this ProtectionRule.
        :type: bool
        """
        self._is_body_inspection_enabled = is_body_inspection_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
