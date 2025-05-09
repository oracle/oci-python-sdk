# coding: utf-8
# Copyright (c) 2016, 2025, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: v1


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SocialIdentityProviderRelayIdpParamMappings(object):
    """
    Relay Param variable for Social IDP
    """

    def __init__(self, **kwargs):
        """
        Initializes a new SocialIdentityProviderRelayIdpParamMappings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param relay_param_key:
            The value to assign to the relay_param_key property of this SocialIdentityProviderRelayIdpParamMappings.
        :type relay_param_key: str

        :param relay_param_value:
            The value to assign to the relay_param_value property of this SocialIdentityProviderRelayIdpParamMappings.
        :type relay_param_value: str

        """
        self.swagger_types = {
            'relay_param_key': 'str',
            'relay_param_value': 'str'
        }
        self.attribute_map = {
            'relay_param_key': 'relayParamKey',
            'relay_param_value': 'relayParamValue'
        }
        self._relay_param_key = None
        self._relay_param_value = None

    @property
    def relay_param_key(self):
        """
        **[Required]** Gets the relay_param_key of this SocialIdentityProviderRelayIdpParamMappings.
        Key or name of the relayParam.

        **Added In:** 2305190132

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The relay_param_key of this SocialIdentityProviderRelayIdpParamMappings.
        :rtype: str
        """
        return self._relay_param_key

    @relay_param_key.setter
    def relay_param_key(self, relay_param_key):
        """
        Sets the relay_param_key of this SocialIdentityProviderRelayIdpParamMappings.
        Key or name of the relayParam.

        **Added In:** 2305190132

        **SCIM++ Properties:**
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param relay_param_key: The relay_param_key of this SocialIdentityProviderRelayIdpParamMappings.
        :type: str
        """
        self._relay_param_key = relay_param_key

    @property
    def relay_param_value(self):
        """
        Gets the relay_param_value of this SocialIdentityProviderRelayIdpParamMappings.
        Value of the relayParam (if defined)

        **Added In:** 2305190132

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The relay_param_value of this SocialIdentityProviderRelayIdpParamMappings.
        :rtype: str
        """
        return self._relay_param_value

    @relay_param_value.setter
    def relay_param_value(self, relay_param_value):
        """
        Sets the relay_param_value of this SocialIdentityProviderRelayIdpParamMappings.
        Value of the relayParam (if defined)

        **Added In:** 2305190132

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param relay_param_value: The relay_param_value of this SocialIdentityProviderRelayIdpParamMappings.
        :type: str
        """
        self._relay_param_value = relay_param_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
