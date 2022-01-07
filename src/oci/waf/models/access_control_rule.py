# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .web_app_firewall_policy_rule import WebAppFirewallPolicyRule
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AccessControlRule(WebAppFirewallPolicyRule):
    """
    Rule that represents Request/Response Access Control.
    Only actions of the following types are allowed to be referenced in this rule:
    * CHECK
    * ALLOW
    * RETURN_HTTP_RESPONSE
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AccessControlRule object with values from keyword arguments. The default value of the :py:attr:`~oci.waf.models.AccessControlRule.type` attribute
        of this class is ``ACCESS_CONTROL`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this AccessControlRule.
            Allowed values for this property are: "ACCESS_CONTROL", "PROTECTION", "REQUEST_RATE_LIMITING", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param name:
            The value to assign to the name property of this AccessControlRule.
        :type name: str

        :param condition_language:
            The value to assign to the condition_language property of this AccessControlRule.
            Allowed values for this property are: "JMESPATH", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type condition_language: str

        :param condition:
            The value to assign to the condition property of this AccessControlRule.
        :type condition: str

        :param action_name:
            The value to assign to the action_name property of this AccessControlRule.
        :type action_name: str

        """
        self.swagger_types = {
            'type': 'str',
            'name': 'str',
            'condition_language': 'str',
            'condition': 'str',
            'action_name': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'condition_language': 'conditionLanguage',
            'condition': 'condition',
            'action_name': 'actionName'
        }

        self._type = None
        self._name = None
        self._condition_language = None
        self._condition = None
        self._action_name = None
        self._type = 'ACCESS_CONTROL'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
