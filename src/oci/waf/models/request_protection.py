# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RequestProtection(object):
    """
    Module that allows to enable OCI-managed protection capabilities for incoming HTTP requests.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new RequestProtection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param rules:
            The value to assign to the rules property of this RequestProtection.
        :type rules: list[oci.waf.models.ProtectionRule]

        :param body_inspection_size_limit_in_bytes:
            The value to assign to the body_inspection_size_limit_in_bytes property of this RequestProtection.
        :type body_inspection_size_limit_in_bytes: int

        :param body_inspection_size_limit_exceeded_action_name:
            The value to assign to the body_inspection_size_limit_exceeded_action_name property of this RequestProtection.
        :type body_inspection_size_limit_exceeded_action_name: str

        """
        self.swagger_types = {
            'rules': 'list[ProtectionRule]',
            'body_inspection_size_limit_in_bytes': 'int',
            'body_inspection_size_limit_exceeded_action_name': 'str'
        }

        self.attribute_map = {
            'rules': 'rules',
            'body_inspection_size_limit_in_bytes': 'bodyInspectionSizeLimitInBytes',
            'body_inspection_size_limit_exceeded_action_name': 'bodyInspectionSizeLimitExceededActionName'
        }

        self._rules = None
        self._body_inspection_size_limit_in_bytes = None
        self._body_inspection_size_limit_exceeded_action_name = None

    @property
    def rules(self):
        """
        Gets the rules of this RequestProtection.
        Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
        ProtectionRules in this array can only use protection Capabilities of REQUEST_PROTECTION_CAPABILITY type.


        :return: The rules of this RequestProtection.
        :rtype: list[oci.waf.models.ProtectionRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this RequestProtection.
        Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
        ProtectionRules in this array can only use protection Capabilities of REQUEST_PROTECTION_CAPABILITY type.


        :param rules: The rules of this RequestProtection.
        :type: list[oci.waf.models.ProtectionRule]
        """
        self._rules = rules

    @property
    def body_inspection_size_limit_in_bytes(self):
        """
        Gets the body_inspection_size_limit_in_bytes of this RequestProtection.
        Maximum size of inspected HTTP message body in bytes. Actions to take if this limit is exceeded are defined in `bodyInspectionSizeLimitExceededActionName`.

        Body inspection maximum size allowed is defined with per-tenancy limit: 8192 bytes.


        :return: The body_inspection_size_limit_in_bytes of this RequestProtection.
        :rtype: int
        """
        return self._body_inspection_size_limit_in_bytes

    @body_inspection_size_limit_in_bytes.setter
    def body_inspection_size_limit_in_bytes(self, body_inspection_size_limit_in_bytes):
        """
        Sets the body_inspection_size_limit_in_bytes of this RequestProtection.
        Maximum size of inspected HTTP message body in bytes. Actions to take if this limit is exceeded are defined in `bodyInspectionSizeLimitExceededActionName`.

        Body inspection maximum size allowed is defined with per-tenancy limit: 8192 bytes.


        :param body_inspection_size_limit_in_bytes: The body_inspection_size_limit_in_bytes of this RequestProtection.
        :type: int
        """
        self._body_inspection_size_limit_in_bytes = body_inspection_size_limit_in_bytes

    @property
    def body_inspection_size_limit_exceeded_action_name(self):
        """
        Gets the body_inspection_size_limit_exceeded_action_name of this RequestProtection.
        References action by name from actions defined in WebAppFirewallPolicy. Executed if HTTP message
        body size exceeds limit set in field `bodyInspectionSizeLimitInBytes`.

        If this field is `null` HTTP message body will inspected up to `bodyInspectionSizeLimitInBytes` and the rest
        will not be inspected by Protection Capabilities.

        Allowed action types:
        * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.


        :return: The body_inspection_size_limit_exceeded_action_name of this RequestProtection.
        :rtype: str
        """
        return self._body_inspection_size_limit_exceeded_action_name

    @body_inspection_size_limit_exceeded_action_name.setter
    def body_inspection_size_limit_exceeded_action_name(self, body_inspection_size_limit_exceeded_action_name):
        """
        Sets the body_inspection_size_limit_exceeded_action_name of this RequestProtection.
        References action by name from actions defined in WebAppFirewallPolicy. Executed if HTTP message
        body size exceeds limit set in field `bodyInspectionSizeLimitInBytes`.

        If this field is `null` HTTP message body will inspected up to `bodyInspectionSizeLimitInBytes` and the rest
        will not be inspected by Protection Capabilities.

        Allowed action types:
        * **RETURN_HTTP_RESPONSE** terminates further execution of modules and rules and returns defined HTTP response.


        :param body_inspection_size_limit_exceeded_action_name: The body_inspection_size_limit_exceeded_action_name of this RequestProtection.
        :type: str
        """
        self._body_inspection_size_limit_exceeded_action_name = body_inspection_size_limit_exceeded_action_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
