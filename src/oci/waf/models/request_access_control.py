# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20210930


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestAccessControl(object):
    """
    Module that allows inspection of HTTP request properties and to return a defined HTTP response.
    In this module, rules with the name 'Default Action' are not allowed, since this name is reserved for default action logs.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestAccessControl object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param default_action_name:
            The value to assign to the default_action_name property of this RequestAccessControl.
        :type default_action_name: str

        :param rules:
            The value to assign to the rules property of this RequestAccessControl.
        :type rules: list[oci.waf.models.AccessControlRule]

        """
        self.swagger_types = {
            'default_action_name': 'str',
            'rules': 'list[AccessControlRule]'
        }
        self.attribute_map = {
            'default_action_name': 'defaultActionName',
            'rules': 'rules'
        }
        self._default_action_name = None
        self._rules = None

    @property
    def default_action_name(self):
        """
        **[Required]** Gets the default_action_name of this RequestAccessControl.
        References an default Action to take if no AccessControlRule was matched. Allowed action types:

        * **ALLOW** continues execution of other modules and their rules.

        * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.


        :return: The default_action_name of this RequestAccessControl.
        :rtype: str
        """
        return self._default_action_name

    @default_action_name.setter
    def default_action_name(self, default_action_name):
        """
        Sets the default_action_name of this RequestAccessControl.
        References an default Action to take if no AccessControlRule was matched. Allowed action types:

        * **ALLOW** continues execution of other modules and their rules.

        * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.


        :param default_action_name: The default_action_name of this RequestAccessControl.
        :type: str
        """
        self._default_action_name = default_action_name

    @property
    def rules(self):
        """
        Gets the rules of this RequestAccessControl.
        Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.


        :return: The rules of this RequestAccessControl.
        :rtype: list[oci.waf.models.AccessControlRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this RequestAccessControl.
        Ordered list of AccessControlRules. Rules are executed in order of appearance in this array.


        :param rules: The rules of this RequestAccessControl.
        :type: list[oci.waf.models.AccessControlRule]
        """
        self._rules = rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
