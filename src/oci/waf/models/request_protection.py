# coding: utf-8
# Copyright (c) 2016, 2022, Oracle and/or its affiliates.  All rights reserved.
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

        """
        self.swagger_types = {
            'rules': 'list[ProtectionRule]'
        }

        self.attribute_map = {
            'rules': 'rules'
        }

        self._rules = None

    @property
    def rules(self):
        """
        Gets the rules of this RequestProtection.
        Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
        ProtectionRules in this array can only use protection cCapabilities of REQUEST_PROTECTION_CAPABILITY type.


        :return: The rules of this RequestProtection.
        :rtype: list[oci.waf.models.ProtectionRule]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """
        Sets the rules of this RequestProtection.
        Ordered list of ProtectionRules. Rules are executed in order of appearance in this array.
        ProtectionRules in this array can only use protection cCapabilities of REQUEST_PROTECTION_CAPABILITY type.


        :param rules: The rules of this RequestProtection.
        :type: list[oci.waf.models.ProtectionRule]
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
